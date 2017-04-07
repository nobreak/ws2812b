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


# strip - the strip object a connected strip
# color1 - first color
# color2 - second color
# countPixelColor1 - count of pixels for color1, the count of pixels for color 2 will be calculated by LED_COUNT. Should be smaller than LED_COUNT
# timeValue - time to switch to the next pixel
def twoColorRotationLamp(strip, color1, color2, countPixelColor1, timeValue):
  f = 1
  # loop for all needed pixels
  while 1: # endless loop	
    # fill the first pixels up to countPixelColor1
    # but only one time (f)
    while f == 1: 
      for h in range(0, countPixelColor1, +1):
        strip.setPixelColor(h,color1)
        strip.show()
        time.sleep(timeValue)
      f = f+1
    # now move the first color to the right and add the second color on the left
    for i in range(countPixelColor1,strip.numPixels(), +1):
      strip.setPixelColor(i, color1)
      strip.setPixelColor(i-countPixelColor1,color2)
      strip.show()
      time.sleep(timeValue)
    
    # the following loop realized the animation of a coolection of pixels
    # with the same color over the end of the strip and starting again
    # at the beginning on the strip
    for k in range(strip.numPixels()-countPixelColor1, strip.numPixels()):
      strip.setPixelColor(k, color2)
      strip.setPixelColor((strip.numPixels()-k-countPixelColor1)*-1, color1)
      strip.show()
      time.sleep(timeValue)
 

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Color wipe animations.
                twoColorRotationLamp(strip, Color(255,0,0), Color(0,0,255), 30, 0.055)
