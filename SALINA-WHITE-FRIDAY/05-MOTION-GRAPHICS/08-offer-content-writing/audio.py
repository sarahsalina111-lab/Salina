# Sound effects for the «يقنع» content-writing course offer. No music.
# Usage: python3 audio.py <out.wav>
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
from sfx import *

CARD, LEARN, GIFT, DISC, CTA = 3.3, 8.0, 11.6, 14.0, 17.4
tr = Track(20.1)
tr.add(0, whoosh(.35), .25)
for i in range(4): tr.add(.2 + i * .1, tick(2200), .12)
for i in range(16): tr.add(.15 + i * .09, tick(3400 + 200 * (i % 3), .025), .1, .2)   # typing
tr.add(.75, fall(700, 300, .4), .2)                                                # deleting, sigh
tr.add(.8, pop(400, 800, .1), .3)
tr.add(1.6, riser(400, 1100, .3), .3); tr.add(1.75, pop(500, 1400, .14), .5); tr.add(1.8, ding(1568, .8), .35)
for i in range(9): tr.add(1.8 + i * .07, pop(900 + 60 * i, 1700 + 60 * i, .05), .14, (i - 4) * .15)
for i in range(3): tr.add(2.0 + i * .2, pop(600, 1200, .08), .3, [.6, -.6, .6][i])
for i in range(3): tr.add(2.0 + i * .1, tick(2000), .14)
tr.add(2.35, impact(), .3)
tr.add(CARD - .3, whoosh(.4, False), .3)
tr.add(CARD + .35, thump(180, .25), .55); tr.add(CARD + .4, tick(1200, .05), .3)
for i in range(5): tr.add(CARD + .6 + i * .32, pop(520 + 50 * i, 1100 + 80 * i, .08), .32, .5)
tr.add(LEARN - .35, whoosh(.45, False), .3)
for i in range(5): tr.add(LEARN + .3 + i * .3, pop(450 + 60 * i, 1000 + 100 * i, .07), .35, -.3)
for i in range(4): tr.add(LEARN + 2.2 + i * .1, tick(2200), .14)
# bonus gift
tr.add(GIFT - .3, whoosh(.4, False), .3); tr.add(GIFT + .05, thump(200, .25), .5)
for i in range(4): tr.add(GIFT + .3 + i * .06, tick(1500, .03), .25)       # box rattles
tr.add(GIFT + .6, pop(300, 1200, .2), .5); tr.add(GIFT + .75, sparkle(86, .06), .45); tr.add(GIFT + .8, riser(500, 1300, .4), .2)
for i in range(4): tr.add(GIFT + 1.1 + i * .12, tick(2300), .14)
tr.add(DISC - .2, whoosh(.7), .5)
for i in range(2): tr.add(DISC + .45 + i * .12, tick(2200), .15)
tr.add(DISC + .75, impact(), .7); tr.add(DISC + .8, kaching(), .45); tr.add(DISC + .9, sparkle(84), .35)
for i in range(3): tr.add(DISC + 1.45 + i * .1, tick(2300), .14)
tr.add(DISC + 1.95, pop(450, 1200, .12), .35)
tr.add(DISC + 2.3, pop(500, 1300, .12), .35)
cta_sfx(tr.add, CTA)
tr.write(sys.argv[1]); print('wrote', sys.argv[1])
