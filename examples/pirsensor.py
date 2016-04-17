import pifacedigitalio
import time

def switch_pressed(event):
    i = 0
    event.chip.output_pins[event.pin_num].turn_on()
    while i <= 5:
        i += 1
        time.sleep(1)
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
    listener.register(0, pifacedigitalio.IODIR_OFF, print_state)
    listener.register(0, pifacedigitalio.IODIR_OFF, switch_pressed)
    listener.activate()
