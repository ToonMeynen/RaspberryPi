#print state op ports (high low)
import pifacedigitalio
pifacedigital = pifacedigitalio.PiFaceDigital()

for i in range(8):
    state = pifacedigital.input_pins[i].value
    print state
