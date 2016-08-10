#!/usr/bin/env python
import pifacedigitalio, time, logging, ephem
from datetime import datetime
logging.basicConfig(filename='/var/log/pir-sensor.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def switch_pressed(event):
    #calculate sunset and sunrise
    o=ephem.Observer()
    o.lat='50'
    o.long='4'
    s=ephem.Sun()
    s.compute()
    sundown = ephem.localtime(o.previous_setting(s))
    sunrise = ephem.localtime(o.next_rising(s))
    #logging.info("sun down", sundown)
    #logging.info("sun up", sunrise)


    if datetime.now() > sundown and datetime.now() < sunrise:
        logging.info('light on')
        i = 0
        event.chip.output_pins[event.pin_num].turn_on()
        time.sleep(20)
        event.chip.output_pins[event.pin_num].turn_off()
    else:
        logging.info('light off: sun is still up')

def switch_unpressed(event):
    event.chip.output_pins[event.pin_num].turn_off()

def print_state(event):
    eventstate = pifacedigital.input_pins[event.pin_num].value
    print "pin", event.pin_num, "is ", eventstate


if __name__ == "__main__":
    pifacedigital = pifacedigitalio.PiFaceDigital()

    listener = pifacedigitalio.InputEventListener(chip=pifacedigital)
    listener.register(0, pifacedigitalio.IODIR_ON, switch_unpressed)
#    listener.register(0, pifacedigitalio.IODIR_OFF, print_state)
    listener.register(0, pifacedigitalio.IODIR_OFF, switch_pressed)
    listener.activate()
