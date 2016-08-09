#!/usr/bin/env python
import ephem
from datetime import datetime
#calculate sundown

o=ephem.Observer()
o.lat='50'
o.long='4'
o.date = datetime.now()
s=ephem.Sun()
s.compute()
sunset = ephem.localtime(o.previous_setting(s))
sunrise = ephem.localtime(o.next_rising(s))
print "sun down ", sunset
print "sun up ",sunrise
print "now ", datetime.now()


if datetime.now() < sunset:
    print "now < sundown"
else:
    print "sundown > now"

if datetime.now() < sunrise:
    print "now < sunrise"
else:
    print "sunsire > now"
