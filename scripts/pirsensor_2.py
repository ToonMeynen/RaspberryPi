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
    sunset = ephem.localtime(o.previous_setting(s))
    sunrise = ephem.localtime(o.next_rising(s))
    now = datetime.now()
    logging.info('provious sunset: {:%H:%M:%S - %m/%d/%Y}'.format(sunset))
    logging.info('next sunrise: {:%H:%M:%S - %m/%d/%Y}'.format(sunrise))
    if datetime.now() >= sunset and datetime.now() <= sunrise:
        logging.info('light on')
        ##Keep the light on when the sensor is active.
        while pifacedigitalio.PiFaceDigital().IODIR_OFF:
            event.chip.output_pins[event.pin_num].turn_on()
            time.sleep(20)
        event.chip.output_pins[event.pin_num].turn_off()
    else:
        logging.info('light off: sun is still up')
    if datetime.now().strftime('%P') == 'am':
    #morning block
        if datetime.now() < sunrise:
            logging.info("sun is still down, light can go on. $now < $sunrise")
            while True:
                event.chip.output_pins[event.pin_num].turn_on()
                time.sleep(10)
                if not pifacedigitalio.PiFaceDigital().IODIR_OFF:
                    break
            event.chip.output_pins[event.pin_num].turn_off()
        else:
            logging.info("sun is up, light needs to stay off $now > $sunrise")
    else:
    #evenning block
        if datetime.now() < sunrise:
            logging.info( "sun is still up, light needs to stay off $now < $sunset")
        else:
            logging.info("sun is down, light can go on. $sunset > $now")
            while True:
                event.chip.output_pins[event.pin_num].turn_on()
                time.sleep(10)
                if not pifacedigitalio.PiFaceDigital().IODIR_OFF:
                    break
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
#    listener.register(0, pifacedigitalio.IODIR_OFF, print_state)
    listener.register(0, pifacedigitalio.IODIR_OFF, switch_pressed)
    listener.activate()
