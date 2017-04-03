# rotation lamp for two colors
# Author: Philipp Homann 
#
import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)



def twoColorRotationLamp(strip, color, color2, numPixel):
  for i in range(numPixel-1, strip.numPixels()):
    strip.setPixelColor(i, color)
    for j in range(i-1, i-numPixel, -1):
      strip.setPixelColor(j, color)
    strip.setPixelColor(i-numPixel, color2)
    strip.show()
    time.sleep(0.0125)
  for k in range(strip.numPixels()-numPixel-1, strip.numPixels()):
    strip.setPixelColor(k, color2)
    strip.setPixelColor((strip.numPixels()-k-numPixel)*-1, color)
    strip.show()
    time.sleep(0.0125)


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Color wipe animations.
                twoColorRotationLamp(strip, Color(0,255,0), Color(0,0,255), 30)
