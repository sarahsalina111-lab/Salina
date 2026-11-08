# Sound effects for video 4 («اشتراكات بتطوّرك»). No music.
# Usage: python3 audio.py <out.wav>
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
from sfx import *

tr = Track(19.9)
tr.add(.05, whoosh(.5), .3)                                   # phone rises
tr.add(.3, tick(2200), .2); tr.add(.48, tick(2000), .2)
tr.add(.85, impact(), .35); tr.add(.85, pop(400, 900, .12), .3)
for i in range(12): tr.add(.55 + i * .11, pop(500 + 40 * i, 1000 + 60 * i, .07), .22, (i % 3 - 1) * .5)
for i in range(6): tr.add(3.2 + i * .05, whoosh(.25, False), .12, (-1) ** i * .7)   # tiles flicked away
tr.add(3.55, thump(220, .18), .4)                             # app bar lands
for t in [3.5, 3.65, 3.8, 3.96]: tr.add(t, tick(2300), .16)
ROW0, ROWD = 4.4, 1.42
for k in range(7):
    s = ROW0 + k * ROWD
    tr.add(s, whoosh(.3), .18, -.4)
    tr.add(s + .05, pop(500, 1000, .08), .25)
    if k < 6:
        tr.add(s + .7, tick(1600, .05), .55); tr.add(s + .71, thump(300, .08), .25)   # switch on
        tr.add(s + .75, riser(380 + 60 * k, 700 + 90 * k, .45), .16, .2)             # level climbs
    else:
        tr.add(s + .1, sparkle(88, .05), .3)
for k in (1, 3, 5): tr.add(ROW0 + k * ROWD + .72, kaching(), .38)                  # level milestones
tr.add(14.9, whoosh(.5, False), .35)
for t in [15.3, 15.46]: tr.add(t, tick(2200), .18)
tr.add(15.75, impact(), .5)
for t in [16.15, 16.27, 16.39]: tr.add(t, tick(2400), .15)
tr.add(16.95, whoosh(.7), .55)
cta_sfx(tr.add, 17.55)
tr.write(sys.argv[1]); print('wrote', sys.argv[1])
