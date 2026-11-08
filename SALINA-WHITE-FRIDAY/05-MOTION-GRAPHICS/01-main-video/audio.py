# Synthesises the soundtrack for the main campaign video: a light 120 BPM music bed + SFX cued to the animation.
# Pure numpy, no samples or external assets. Output: 48 kHz stereo 16-bit WAV.
# Usage: python3 audio.py <out.wav>
import sys, wave
import numpy as np

SR = 48000
DUR = 20.0
N = int(SR * DUR)
rng = np.random.default_rng(7)
music = np.zeros((N, 2)); sfx = np.zeros((N, 2))

def t_(d): return np.arange(int(SR * d)) / SR
def env(n, a=.005, r=.2):
    t = np.arange(n) / SR; e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r); return e
def add(buf, start, sig, gain=1.0, pan=0.0):
    i = int(start * SR); sig = sig[: max(0, len(buf) - i)]
    if i < 0 or not len(sig): return
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    buf[i:i + len(sig), 0] += sig * gain * l * 1.414; buf[i:i + len(sig), 1] += sig * gain * r * 1.414
def lowpass(x, a):  # one-pole
    y = np.empty_like(x); acc = 0.0
    for i, v in enumerate(x): acc += a * (v - acc); y[i] = acc
    return y
def midi(n): return 440 * 2 ** ((n - 69) / 12)

# ---------------- SFX ----------------
def pop(f0=500, f1=1100, d=.12):
    t = t_(d); f = np.geomspace(f0, f1, len(t)); ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * env(len(t), .002, d / 4)
def thump(f0=150, d=.25):
    t = t_(d); f = np.geomspace(f0, 45, len(t)); ph = 2 * np.pi * np.cumsum(f) / SR
    click = rng.standard_normal(len(t)) * np.exp(-t / .004) * .3
    return (np.sin(ph) * env(len(t), .001, .08) + click)
def whoosh(d=.7, rise=True):
    n = int(SR * d); x = rng.standard_normal(n); t = np.arange(n) / SR
    a = np.linspace(.02, .25, n) if rise else np.linspace(.25, .02, n)
    y = np.empty(n); acc = 0.0
    for i in range(n): acc += a[i] * (x[i] - acc); y[i] = acc
    shape = np.sin(np.pi * np.clip(t / d, 0, 1)) ** 2
    return y * shape * 2.2
def ding(f=1318.5, d=1.4):
    t = t_(d); s = sum(np.sin(2 * np.pi * f * k * t) * w * np.exp(-t / (d / (1 + 2 * i)))
                     for i, (k, w) in enumerate([(1, 1), (2.76, .4), (5.4, .18), (8.9, .08)]))
    return s * env(len(t), .002, 10)
def tick(f=2400, d=.04):
    t = t_(d); return np.sin(2 * np.pi * f * t) * np.exp(-t / .008)
def riser(f0=260, f1=980, d=.8):
    t = t_(d); f = np.geomspace(f0, f1, len(t)); ph = 2 * np.pi * np.cumsum(f) / SR
    tri = 2 / np.pi * np.arcsin(np.sin(ph)); return tri * np.sin(np.pi * t / d) ** .7 * .6
def sparkle(base=84, d=.09):
    out = np.zeros(int(SR * 1.2))
    for k, n in enumerate([0, 4, 7, 12, 16]):
        s = ding(midi(base + n), .7) * .5; i = int(k * d * SR); out[i:i + len(s)] += s[: len(out) - i]
    return out
def impact():
    t = t_(.6); body = np.sin(2 * np.pi * np.cumsum(np.geomspace(110, 38, len(t))) / SR) * env(len(t), .001, .18)
    noise = lowpass(rng.standard_normal(len(t)), .2) * np.exp(-t / .05)
    return body * 1.2 + noise * 1.5

# scene 1: bags land, items pop out, words tick in
for tl, pan in [(.55, -.5), (1.0, 0), (1.45, .5)]: add(sfx, tl, thump(), .7, pan); add(sfx, tl - .3, whoosh(.3), .25, pan)
ITEM_T = [(1.75, -.5), (1.95, 0), (2.15, .5), (2.35, -.4), (2.55, .4), (2.75, -.6), (2.95, .6), (3.15, .1)]
for k, (tp, pan) in enumerate(ITEM_T): add(sfx, tp, pop(400 + 45 * k, 950 + 90 * k), .55, pan)
def kaching():  # discount sticker: short register bell
    return np.concatenate([ding(2093, .25) * .6, np.zeros(int(.05 * SR))])[: int(.3 * SR)] + np.pad(ding(2637, .5), (int(.07 * SR), 0))[: int(.3 * SR)]
for tp, pan in [(2.3, -.7), (2.75, .7), (3.2, -.2)]: add(sfx, tp, kaching(), .32, pan)
for k in range(9): add(sfx, 2.45 + k * .21 + .05 * (k % 2), tick(3800 + 300 * (k % 3), .03), .06, (-1) ** k * .6)  # sparkle shimmer
for tw in [.35, .49, .63, .85, 3.25, 3.41, 3.57]: add(sfx, tw, tick(), .18)
# scene 2: crowd, gulp into one bag, fill, items out, bulb on
add(sfx, 4.1, whoosh(.55), .35)
for k in range(8): add(sfx, 4.62 + k * .085 + .38, pop(950 - 60 * k, 400 - 25 * k, .09), .4, (k - 3.5) * .15)
for i in range(3): add(sfx, 5.0 + i * .1 + .36, pop(1200, 500, .08), .3)
add(sfx, 5.2, whoosh(.5, False), .3)
add(sfx, 6.05, riser(), .45)
add(sfx, 6.85, thump(180, .3), .8); add(sfx, 6.85, pop(300, 900, .15), .4)
for k, tp in enumerate([7.0, 7.3, 7.6]): add(sfx, tp, pop(520 + 100 * k, 1300 + 150 * k), .55, (k - 1) * .4)
add(sfx, 8.02, ding(), .55, .3)
# scene 3: bag settles, words, dots, the «استثمري» hit
add(sfx, 9.0, whoosh(.6, False), .3)
for tw in [9.1, 9.32]: add(sfx, tw, tick(2000), .2)
for k in range(3): add(sfx, 9.55 + k * .15, pop(700 + 150 * k, 1500 + 200 * k, .08), .4)
add(sfx, 10.3, impact(), .85); add(sfx, 10.55, whoosh(.35), .35, -.3)
for tw in [11.05, 11.25]: add(sfx, tw, tick(1800), .22)
add(sfx, 11.5, pop(500, 1600, .14), .5, .3)
add(sfx, 12.4, pop(350, 700, .1), .25)
# scene 4: purple circle opens, letters, closing chime
add(sfx, 13.35, whoosh(.85), .6)
for k in range(6): add(sfx, 14.2 + k * .07, tick(1600 + 120 * k), .22, (k - 2.5) * .15)
add(sfx, 14.75, whoosh(.5), .25)
for tw in [15.45, 15.63, 16.0, 16.16, 16.32]: add(sfx, tw, tick(2200), .16)
add(sfx, 16.55, sparkle(), .45)
# end card (CTA) — same cues as lib/sfx.py cta_sfx
import os as _os; sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'lib'))
import sfx as _lib
_lib.cta_sfx(lambda st, sig, g=1.0, pan=0.0: add(sfx, st, sig, g, pan), 17.6)

# ---------------- MUSIC (120 BPM, C major, I–vi–IV–V) ----------------
BEAT = .5
chords = [[60, 64, 67], [57, 60, 64], [53, 57, 60], [55, 59, 62]]
bass_notes = [36, 33, 29, 31]
def pluck(f, d=.32):
    t = t_(d); ph = 2 * np.pi * f * t
    s = .6 * np.sin(ph) + .25 * np.sin(2 * ph) + .1 * np.sin(3 * ph)
    return s * env(len(t), .003, .12)
def bass(f, d=.45):
    t = t_(d); return (np.sin(2 * np.pi * f * t) + .3 * np.sin(4 * np.pi * f * t)) * env(len(t), .005, .25)
def kick():
    t = t_(.3); f = np.geomspace(120, 42, len(t)); return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(t), .001, .09)
def clap():
    t = t_(.2); n = lowpass(rng.standard_normal(len(t)), .5) - lowpass(rng.standard_normal(len(t)), .05)
    e = sum(np.exp(-np.clip(t - d, 0, None) / .02) * (t >= d) for d in (0, .012, .024)); return n * e * .7
def shaker():
    t = t_(.06); n = rng.standard_normal(len(t)); n = n - lowpass(n, .3); return n * np.exp(-t / .015)

MUSIC = False   # the client asked for sound effects only
END_MUSIC = 17.2
for bar in (range(10) if MUSIC else []):
    t0 = bar * 4 * BEAT; ch = chords[bar % 4]
    for b in range(4):
        tb = t0 + b * BEAT
        if tb > END_MUSIC: break
        # a pause for «المرة دي...» (8.9–10.3), music returns on the «استثمري» hit
        if 8.9 <= tb < 10.3: continue
        full = tb >= 10.3
        add(music, tb, kick(), .55 if b % 2 == 0 else .0)
        if b % 2 == 1: add(music, tb, clap(), .28)
        add(music, tb, bass(midi(bass_notes[bar % 4])), .35)
        for e8 in range(2):
            te = tb + e8 * BEAT / 2
            if 8.9 <= te < 10.3: continue
            note = ch[(b * 2 + e8) % 3] + 12 + (12 if (full and e8) else 0)
            add(music, te, pluck(midi(note)), .16, -.35 if e8 else .35)
            add(music, te, shaker(), .07, .5)
# closing chord
for n in ([48, 60, 64, 67, 72] if MUSIC else []): add(music, 16.55, pluck(midi(n), 2.2) * np.exp(-t_(2.2) / 1.2), .14)
# gentle fade in / out
fade = np.ones(N); fi = int(.25 * SR); fade[:fi] = np.linspace(0, 1, fi); fo = int(1.4 * SR); fade[-fo:] = np.linspace(1, 0, fo)
music *= fade[:, None]

mix = (music * .55 if MUSIC else 0) + sfx * .9
mix /= np.max(np.abs(mix)) / .89            # peak ≈ -1 dBFS
pcm = (mix * 32767).astype('<i2')
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('wrote', sys.argv[1], f'{DUR}s')
