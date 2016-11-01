#Talk to your raspberrypi using jasper.
__author__ = 'Toon Meynen'
import pifacedigitalio
pfd = pifacedigitalio.PiFaceDigital() # creates a PiFace Digtal object
WORDS = ["dance"]
PRIORITY = 1
def is_valid(text):
    """
        Returns True if the input is related to "dance".

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bdance\b', text, re.IGNORECASE))


def handle(text, mic, profile):
    """
        Makes PiBot dance

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone number)
    """
    line = "Toggle light"
    mic.say(line)  # Tell the user to watch my dance moves
    pfd.leds[0].toggle() # toggle third LED
