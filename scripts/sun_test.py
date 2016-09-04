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
now = datetime.now()
print "sun down ", sunset
print "sun up ",sunrise
print "now ", datetime.now()
print '{:%H:%M:%S - %m/%d/%Y}'.format(sunset)

if datetime.now().strftime('%P') == 'am':
#morning block
    if datetime.now() < sunrise:
        print "sun is still down, light can go on. $now < $sunrise"
    else:
        print "sun is up, light needs to stay off $now > $sunrise"
else:
#evenning block
    if datetime.now() < sunrise:
        print "sun is still up, light needs to stay off $now < $sunset"
    else:
        print "sun is down, light can go on. $sunset > $now"
