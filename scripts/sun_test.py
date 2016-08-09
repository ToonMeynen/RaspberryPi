import ephem
from datetime import datetime
#calculate sundown

o=ephem.Observer()
o.lat='50'
o.long='4'
s=ephem.Sun()
s.compute()
sundown = ephem.localtime(o.next_setting(s))
sunrise = ephem.localtime(o.next_rising(s))
print "sun down ", sundown
print "sun up ",sunrise

if datetime.now() > sundown and datetime.now() < sunrise:
    print "light goes on"
else:
    print "ligt stays off"
