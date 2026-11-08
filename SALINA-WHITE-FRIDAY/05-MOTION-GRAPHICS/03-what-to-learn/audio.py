# Sound effects for video 3 («إيه اللي نفسك تتعلميه؟» — add to cart). No music.
# Usage: python3 audio.py <out.wav>
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
from sfx import *

tr = Track(19.9)
# hook
tr.add(.25, tick(2200), .2); tr.add(.45, tick(2000), .2)
tr.add(.7, impact(), .45); tr.add(.7, pop(400, 1000, .12), .3)
tr.add(1.15, pop(500, 1300, .14), .45)
for k in range(4): tr.add(1.4 + k * .1, pop(900 + 150 * k, 1700 + 150 * k, .07), .25, (-1) ** k * .6)
tr.add(2.15, whoosh(.4, False), .3)
tr.add(2.45, thump(200, .2), .45, -.6)          # cart lands
tr.add(2.35, whoosh(.3), .15)
CARD0, CARD = 2.8, 3.0
for k in range(4):
    s = CARD0 + k * CARD
    tr.add(s - .05, whoosh(.5), .35, -.5)                     # card slides in
    tr.add(s + .4, pop(700, 1400, .07), .3)                   # chip
    for i in range(3): tr.add(s + .5 + i * .1, tick(2300), .14)
    tr.add(s + 1.3, pop(450, 1100, .12), .4)                  # button
    tr.add(s + 1.88, tick(1700, .05), .55); tr.add(s + 1.9, thump(260, .1), .3)   # tap
    tr.add(s + 2.0, whoosh(.5), .25, -.4)                     # flies to the cart
    tr.add(s + 2.5, kaching(), .4, -.6)                       # lands, counter +1
    tr.add(s + 2.62, whoosh(.4, False), .25, .5)              # card slides out
    if k == 0:
        for i in range(10): tr.add(s + .6 + i * .18, tick(3000 + 200 * (i % 3), .025), .12)   # pen scratches
        tr.add(s + .55, pop(300, 600, .15), .3, .5)
    if k == 1:
        for i, d in enumerate([.7, 1.0]): tr.add(s + d, pop(900 + 300 * i, 1800 + 300 * i, .06), .35, (-1) ** i * .4)
        tr.add(s + 1.25, pop(500, 900, .1), .3, .4)
    if k == 2:
        tr.add(s + 1.22, impact(), .35); tr.add(s + 1.22, tick(900, .05), .6)   # clapper
        for i in range(4): tr.add(s + .3 + i * .66, tick(4000, .02), .08)        # REC blink
    if k == 3:
        tr.add(s + .3, riser(300, 600, .4), .12)
        tr.add(s + 1.05, sparkle(88, .05), .3, .4)
        for i in range(4): tr.add(s + .9 + i * .45, pop(800, 1300, .06), .15, (-1) ** i * .5)
# summary
tr.add(14.8, whoosh(.6), .35)
tr.add(15.4, kaching(), .4)
for i in range(3): tr.add(15.4 + i * .14, tick(2200), .18)
tr.add(15.9, impact(), .5)
tr.add(16.95, whoosh(.7), .55)
cta_sfx(tr.add, 17.55)
tr.write(sys.argv[1]); print('wrote', sys.argv[1])
