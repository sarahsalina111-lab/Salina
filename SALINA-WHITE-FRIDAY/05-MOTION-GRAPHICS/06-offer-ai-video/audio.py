# Sound effects for the AI video-making workshop offer. No music.
# Usage: python3 audio.py <out.wav>
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
from sfx import *

CARD, LEARN, DISC, CTA = 3.3, 7.2, 11.4, 14.8
def knock():  # wooden knock
    t = t_(.18); body = np.sin(2 * np.pi * np.cumsum(np.geomspace(260, 140, len(t))) / SR) * env(len(t), .001, .03)
    return body * 1.4 + lowpass(rng.standard_normal(len(t)), .3) * np.exp(-t / .01) * .6
def creak(d=.5):
    t = t_(d); f = 180 + 60 * np.sin(2 * np.pi * 7 * t); ph = 2 * np.pi * np.cumsum(f) / SR
    return (2 / np.pi * np.arcsin(np.sin(ph))) * env(len(t), .05, d / 2) * .35
tr = Track(17.5)
tr.add(0, whoosh(.35), .25)
for i in range(6): tr.add(.15 + i * .1, tick(2200), .12)
for t0 in (.35, .7):
    tr.add(t0, knock(), .9); tr.add(t0 + .11, knock(), .75)
    tr.add(t0, pop(500, 900, .08), .2)
tr.add(1.15, creak(), .5); tr.add(1.5, sparkle(84, .05), .3)
tr.add(1.35, impact(), .3)
for i in range(3): tr.add(2.0 + i * .1, tick(2000), .14)
tr.add(2.35, pop(500, 1100, .12), .35)
tr.add(CARD - .3, whoosh(.4, False), .3)
tr.add(CARD + .35, thump(180, .25), .55); tr.add(CARD + .4, tick(1200, .05), .3)
for i in range(3): tr.add(CARD + .6 + i * .32, pop(520 + 60 * i, 1100 + 90 * i, .08), .35, .5)
tr.add(LEARN - .35, whoosh(.45, False), .3)
for i in range(4): tr.add(LEARN + .1 + i * .1, tick(2200), .12)
for i in range(6): tr.add(LEARN + .3 + i * .38, pop(450 + 70 * i, 1000 + 120 * i, .08), .4, -.3)
for i in range(4): tr.add(LEARN + 2.75 + i * .1, tick(2200), .14)
tr.add(DISC - .2, whoosh(.7), .5)
for i in range(2): tr.add(DISC + .45 + i * .12, tick(2200), .15)
tr.add(DISC + .75, impact(), .7); tr.add(DISC + .8, kaching(), .45); tr.add(DISC + .9, sparkle(84), .35)
for i in range(4): tr.add(DISC + 1.45 + i * .1, tick(2300), .14)
tr.add(DISC + 1.95, pop(450, 1200, .12), .35)
tr.add(DISC + 2.3, pop(500, 1300, .12), .35)
cta_sfx(tr.add, CTA)
tr.write(sys.argv[1]); print('wrote', sys.argv[1])
