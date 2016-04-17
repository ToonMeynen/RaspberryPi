from time import sleep
import pifacedigitalio


DELAY = 1.0  # seconds


if __name__ == "__main__":
    p = pifacedigitalio.PiFaceDigital()

for i in range(6):
    p.output_pins[i].turn_off()
try:
    pin = int(raw_input('enter an input between 0 and 7: '))
except:
    print 'please enter a valid rate'
    exit()
   
p.leds[pin].toggle()
if p.leds[pin].value == 1:
    print "led", pin, "is high, pin"
else:
    print "led", pin, "is low, pin"    
