#!/usr/bin/env python
import pifacedigitalio, time, logging, ephem
from datetime import datetime
logging.basicConfig(filename='/var/log/pir-sensor.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def switch_pressed(event):
    #calculate sunset and sunrise
    o=ephem.Observer()
    o.lat='50'
    o.long='4'
    s=ephem.Sun()
    s.compute()
    sunrise = ephem.localtime(o.previous_rising(s))
    sunset = ephem.localtime(o.previous_setting(s))
    now = datetime.now()

    logging.info('Sunrise: {:%H:%M:%S - %m/%d/%Y}'.format(sunrise))
    logging.info('Sunset: {:%H:%M:%S - %m/%d/%Y}'.format(sunset))

    if datetime.now().strftime('%p') == 'AM':
    #morning block
        if datetime.now() < sunrise:
            logging.info("Sun is still down, light can go on.")
            event.chip.output_pins[event.pin_num].turn_on()
            time.sleep( 20 )
            event.chip.output_pins[event.pin_num].turn_off()
        else:
            logging.info("Sun is up, light needs to stay off.")
    else:
    #evenning block
        if datetime.now() < sunset:
            logging.info('Sunrise: {:%H:%M:%S - %m/%d/%Y}'.format(sunrise))
            logging.info('Sunset: {:%H:%M:%S - %m/%d/%Y}'.format(sunset))
            logging.info( "Sun is still up, light needs to stay off.")
        else:
            logging.info("Sun is down, light can go on.")
            event.chip.output_pins[event.pin_num].turn_on()
            time.sleep( 20 )
            event.chip.output_pins[event.pin_num].turn_off()

def switch_unpressed(event):
    event.chip.output_pins[event.pin_num].turn_off()

def print_state(event):
    eventstate = pifacedigital.input_pins[event.pin_num].value
    print "pin", event.pin_num, "is ", eventstate


if __name__ == "__main__":
    pifacedigital = pifacedigitalio.PiFaceDigital()

    listener = pifacedigitalio.InputEventListener(chip=pifacedigital)
    listener.register(0, pifacedigitalio.IODIR_ON, switch_unpressed)
    # listener.register(0, pifacedigitalio.IODIR_OFF, print_state)
    listener.register(0, pifacedigitalio.IODIR_OFF, switch_pressed)
    listener.activate()
