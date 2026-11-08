# Sound effects for the «AI in education» course offer. No music.
# Usage: python3 audio.py <out.wav>
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
from sfx import *

CARD, LEARN, DISC, CTA = 3.3, 8.2, 13.5, 16.9
tr = Track(19.6)
tr.add(0, whoosh(.35), .25)
for i in range(5): tr.add(.2 + i * .1, tick(2200), .12)
for i in range(9): tr.add(.1 + i * .06, pop(400 + 30 * i, 700 + 40 * i, .06), .15, -.5)   # papers stack up
for i in range(14): tr.add(.25 + i * .08, clock_tick(), .2, .5)                             # clock races
for i in range(3): tr.add(.5 + i * .25, pop(300, 600, .1), .3, .4)                          # mugs
tr.add(1.35, riser(300, 900, .4), .3); tr.add(1.4, pop(500, 1300, .14), .45)                # AI laptop
tr.add(1.45, whoosh(.5), .35)                                                               # papers sucked in
tr.add(1.95, pop(600, 1300, .12), .4)
for k in range(3): tr.add(2.2 + k * .15, tick(1700, .05), .35)                              # check marks
tr.add(2.3, ding(1568, .9), .3)
for i in range(3): tr.add(2.0 + i * .1, tick(2000), .14)
tr.add(2.35, pop(500, 1100, .12), .35)
tr.add(CARD - .3, whoosh(.4, False), .3)
tr.add(CARD + .35, thump(180, .25), .55); tr.add(CARD + .4, tick(1200, .05), .3)
for i in range(6): tr.add(CARD + .6 + i * .32, pop(520 + 50 * i, 1100 + 80 * i, .08), .32, .5)
tr.add(LEARN - .35, whoosh(.45, False), .3)
for i in range(3): tr.add(LEARN + .1 + i * .1, tick(2200), .12)
for i in range(9): tr.add(LEARN + .3 + i * .3, pop(450 + 50 * i, 950 + 90 * i, .07), .35, -.3)
for i in range(4): tr.add(LEARN + 3.3 + i * .1, tick(2200), .14)
tr.add(DISC - .2, whoosh(.7), .5)
for i in range(2): tr.add(DISC + .45 + i * .12, tick(2200), .15)
tr.add(DISC + .75, impact(), .7); tr.add(DISC + .8, kaching(), .45); tr.add(DISC + .9, sparkle(84), .35)
for i in range(5): tr.add(DISC + 1.45 + i * .1, tick(2300), .14)
tr.add(DISC + 1.95, pop(450, 1200, .12), .35)
tr.add(DISC + 2.3, pop(500, 1300, .12), .35)
cta_sfx(tr.add, CTA)
tr.write(sys.argv[1]); print('wrote', sys.argv[1])
