import pifacedigitalio
import time
import os

pifacedigital = pifacedigitalio.PiFaceDigital()

while True:
    for i in range(8):
        state = pifacedigital.input_pins[i].value
        print "pin ", i, "is ", state 
    time.sleep(1)
    os.system('clear')    
