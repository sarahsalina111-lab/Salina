# Shared sound-effect synthesiser for SALINA WHITE FRIDAY videos (numpy only, no samples).
import wave
import numpy as np

SR = 48000
rng = np.random.default_rng(7)

def t_(d): return np.arange(int(SR * d)) / SR
def env(n, a=.005, r=.2):
    t = np.arange(n) / SR; return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)
def lowpass(x, a):
    y = np.empty_like(x); acc = 0.0
    for i, v in enumerate(x): acc += a * (v - acc); y[i] = acc
    return y
def midi(n): return 440 * 2 ** ((n - 69) / 12)

class Track:
    def __init__(self, dur): self.buf = np.zeros((int(SR * dur), 2))
    def add(self, start, sig, gain=1.0, pan=0.0):
        i = int(start * SR); sig = sig[: max(0, len(self.buf) - i)]
        if i < 0 or not len(sig): return
        l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
        self.buf[i:i + len(sig), 0] += sig * gain * l * 1.414; self.buf[i:i + len(sig), 1] += sig * gain * r * 1.414
    def write(self, path, peak=.89):
        mix = self.buf / (np.max(np.abs(self.buf)) / peak)
        with wave.open(path, 'wb') as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype('<i2').tobytes())

def pop(f0=500, f1=1100, d=.12):
    t = t_(d); ph = 2 * np.pi * np.cumsum(np.geomspace(f0, f1, len(t))) / SR
    return np.sin(ph) * env(len(t), .002, d / 4)
def thump(f0=150, d=.25):
    t = t_(d); ph = 2 * np.pi * np.cumsum(np.geomspace(f0, 45, len(t))) / SR
    return np.sin(ph) * env(len(t), .001, .08) + rng.standard_normal(len(t)) * np.exp(-t / .004) * .3
def whoosh(d=.7, rise=True):
    n = int(SR * d); x = rng.standard_normal(n); t = np.arange(n) / SR
    a = np.linspace(.02, .25, n) if rise else np.linspace(.25, .02, n)
    y = np.empty(n); acc = 0.0
    for i in range(n): acc += a[i] * (x[i] - acc); y[i] = acc
    return y * np.sin(np.pi * np.clip(t / d, 0, 1)) ** 2 * 2.2
def ding(f=1318.5, d=1.4):
    t = t_(d); s = sum(np.sin(2 * np.pi * f * k * t) * w * np.exp(-t / (d / (1 + 2 * i)))
                     for i, (k, w) in enumerate([(1, 1), (2.76, .4), (5.4, .18), (8.9, .08)]))
    return s * env(len(t), .002, 10)
def tick(f=2400, d=.04):
    t = t_(d); return np.sin(2 * np.pi * f * t) * np.exp(-t / .008)
def riser(f0=260, f1=980, d=.8):
    t = t_(d); ph = 2 * np.pi * np.cumsum(np.geomspace(f0, f1, len(t))) / SR
    return 2 / np.pi * np.arcsin(np.sin(ph)) * np.sin(np.pi * t / d) ** .7 * .6
def fall(f0=900, f1=250, d=.5):  # descending "deflate" tone
    t = t_(d); ph = 2 * np.pi * np.cumsum(np.geomspace(f0, f1, len(t))) / SR
    return 2 / np.pi * np.arcsin(np.sin(ph)) * env(len(t), .01, d / 2.5) * .6
def sparkle(base=84, step=.09):
    out = np.zeros(int(SR * 1.2))
    for k, n in enumerate([0, 4, 7, 12, 16]):
        s = ding(midi(base + n), .7) * .5; i = int(k * step * SR); out[i:i + len(s)] += s[: len(out) - i]
    return out
def impact():
    t = t_(.6); body = np.sin(2 * np.pi * np.cumsum(np.geomspace(110, 38, len(t))) / SR) * env(len(t), .001, .18)
    return body * 1.2 + lowpass(rng.standard_normal(len(t)), .2) * np.exp(-t / .05) * 1.5
def kaching():
    a = ding(2093, .25) * .6; b = np.pad(ding(2637, .5), (int(.07 * SR), 0)); n = int(.3 * SR)
    return np.pad(a, (0, max(0, n - len(a))))[:n] + b[:n]
def poof(d=.35):
    t = t_(d); return lowpass(rng.standard_normal(len(t)), .08) * env(len(t), .02, .08) * 3
def flip():
    t = t_(.12); c = np.zeros(len(t)); k = tick(1400, .05); c[:len(k)] = k
    return lowpass(rng.standard_normal(len(t)), .4) * np.exp(-t / .02) * 1.2 + c * .5
def clock_tick():
    return tick(3200, .03) * .8

# ---- end card (CTA) ----
def cta_sfx(add, c):
    add(c, whoosh(.35, False), .3)
    for i in range(3): add(c + .2 + i * .12, tick(2200), .18)
    add(c + .5, pop(500, 1150, .12), .45)
    add(c + .7, whoosh(.4), .12, .5)
    add(c + 1.15, impact(), .55); add(c + 1.15, fall(1300, 400, .25), .25)
    add(c + 1.55, pop(450, 1300, .14), .5, -.3)
    add(c + 2.05, tick(1800, .05), .5); add(c + 2.06, thump(260, .12), .3)
