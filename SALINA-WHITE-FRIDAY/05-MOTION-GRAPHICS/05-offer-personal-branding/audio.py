# Sound effects for the Personal Branding offer video. No music.
# Usage: python3 audio.py <out.wav>
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
from sfx import *

CARD, LEARN, DISC, CTA = 3.3, 8.7, 12.5, 15.9
tr = Track(18.6)
# hook: words, the crowd pops in, one face lights up
for i in range(6): tr.add(.2 + i * .1, tick(2200), .14)
for i in range(20): tr.add(.2 + i * .03, pop(600 + 25 * i, 1000 + 40 * i, .05), .08, ((i % 5) - 2) * .3)
tr.add(.75, impact(), .35)
tr.add(1.3, riser(400, 900, .4), .25); tr.add(1.6, ding(1568, 1.0), .45); tr.add(1.65, sparkle(88, .05), .25)
for i in range(4): tr.add(2.0 + i * .1, tick(2000), .14)
tr.add(2.35, pop(500, 1100, .12), .35)
# the workshop tag drops in, facts tick in, audience chips pop
tr.add(CARD - .3, whoosh(.4, False), .3)
tr.add(CARD + .35, thump(180, .25), .55); tr.add(CARD + .4, tick(1200, .05), .3)
for i in range(5): tr.add(CARD + .6 + i * .32, pop(520 + 60 * i, 1100 + 90 * i, .08), .35, .5)
for i in range(5): tr.add(CARD + 2.6 + i * .16, pop(800 + 80 * i, 1500 + 80 * i, .06), .25, (-1) ** i * .4)
# what you learn
tr.add(LEARN - .35, whoosh(.45, False), .3)
for i, d in enumerate([.3, .85]): tr.add(LEARN + d, whoosh(.4), .3, (-1) ** i * .6)
for i in range(2):
    for j in range(4): tr.add(LEARN + .8 + i * .55 + j * .15, pop(900 + 60 * j, 1600 + 60 * j, .05), .2)
for i in range(4): tr.add(LEARN + 2.4 + i * .1, tick(2200), .14)
# the discount
tr.add(DISC - .2, whoosh(.7), .5)
for i in range(2): tr.add(DISC + .45 + i * .12, tick(2200), .15)
tr.add(DISC + .75, impact(), .7); tr.add(DISC + .8, kaching(), .45); tr.add(DISC + .9, sparkle(84), .35)
for i in range(4): tr.add(DISC + 1.45 + i * .1, tick(2300), .14)
tr.add(DISC + 1.95, pop(450, 1200, .12), .35)
tr.add(DISC + 2.3, pop(500, 1300, .12), .35)
cta_sfx(tr.add, CTA)
tr.write(sys.argv[1]); print('wrote', sys.argv[1])
