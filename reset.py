
# rotation lamp for two colors
# Author: Philipp Homann 
#
import time

from neopixel import *
from thread import start_new_thread
from threading import Thread

# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels on stripe.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_TIME       = 0.035   # animation time (time from one pixel to the next
LED_START_PIXEL = 0     # where we want to start the animation on stripe
LED_END_PIXEL = 12      # where we want to end the animation on strip



# set all pixel aof stripe back to black
def reset(strip):
  for pixel in range(strip.numPixels()):
    strip.setPixelColor(pixel,Color(0,0,0))
  strip.show()



# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Color wipe animations.
		reset(strip)
