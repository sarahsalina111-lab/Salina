# Sound effects for video 2 (Shopping vs. Learning). No music, as requested.
# Usage: python3 audio.py <out.wav>
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
from sfx import *

tr = Track(20.4)
# intro: words, then the screen splits
for t in [.3, .5, .95]: tr.add(t, tick(2200), .2)
tr.add(1.85, whoosh(.4, False), .25)
tr.add(2.0, whoosh(.6), .45, -.4)
tr.add(2.35, riser(400, 1200, .5), .2)
for t, pan in [(2.6, .5), (2.7, -.5)]: tr.add(t, pop(600, 1200, .08), .3, pan)
# day of purchase
tr.add(2.95, pop(500, 1100, .12), .4)                       # chip
tr.add(3.15, thump(), .7, .5); tr.add(3.25, thump(), .7, -.5)  # both baskets land
for k, t in enumerate([3.3, 3.55, 3.8]): tr.add(t, pop(450 + 80 * k, 1100 + 150 * k), .5, .6)
tr.add(3.6, pop(700, 1500), .45, -.6)                       # laptop
tr.add(3.6, riser(300, 700, .6), .15, .5)                   # joy meter fills
tr.add(3.7, riser(300, 500, .5), .12, -.5)                  # skill meter starts
tr.add(4.0, kaching(), .3, .6)
tr.add(4.3, tick(2600), .2, .5); tr.add(4.3, tick(2000), .2, -.5)
for k in range(8): tr.add(4.1 + k * .32, tick(3800 + 300 * (k % 3), .03), .06, .7)
# a month later
tr.add(7.0, flip(), .55); tr.add(7.0, clock_tick(), .4)
for k in range(3): tr.add(7.25 + k * .15, fall(1100 - 100 * k, 500, .35), .2, .6)  # tags drop
tr.add(7.35, fall(800, 300, .7), .3, .6)                    # joy meter drops
tr.add(7.4, pop(520, 1250), .5, -.6); tr.add(7.7, pop(620, 1400), .5, -.6)
tr.add(7.6, riser(350, 900, .7), .2, -.5)                   # skill meter rises
tr.add(8.02, ding(), .5, -.5)                               # bulb on
tr.add(7.7, tick(2600), .2, .5); tr.add(7.7, tick(2000), .2, -.5)
# a year later
tr.add(10.6, flip(), .55); tr.add(10.6, clock_tick(), .4)
tr.add(10.9, poof(), .6, .5); tr.add(11.15, poof(), .6, .7)
tr.add(10.9, fall(700, 180, .9), .3, .6)                    # joy meter empties
tr.add(11.0, fall(500, 150, .6), .25, .6)                   # bag deflates
tr.add(11.0, impact(), .35, -.5); tr.add(11.0, pop(400, 1400, .15), .45, -.5)  # certificate
tr.add(11.1, riser(400, 1300, .7), .25, -.5)                # skill meter full
tr.add(11.3, sparkle(84), .4, -.5)
tr.add(11.35, tick(1500, .05), .25, .6); tr.add(11.6, tick(1300, .05), .15, .6)  # hanger swing
tr.add(11.2, tick(2600), .2, .5); tr.add(11.2, tick(2000), .2, -.5)
# outro
tr.add(14.15, whoosh(.8), .55)
for t in [15.0, 15.18, 15.55, 15.75]: tr.add(t, tick(2200), .18)
tr.add(16.35, whoosh(.4), .2)
for t in [16.5, 16.64, 16.78]: tr.add(t, tick(2400), .16)
tr.add(17.05, sparkle(), .45)
cta_sfx(tr.add, 18.0)
tr.write(sys.argv[1])
print('wrote', sys.argv[1])
