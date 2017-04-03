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
# countPixelColor1 - count of pixels for color1, the count of pixels for color 2 will be calculated by LED_COUNT
def twoColorRotationLamp(strip, color1, color2, countPixelColor1):
  # loop for all needed pixels
  for i in range(countPixelColor1-1, strip.numPixels()):
    strip.setPixelColor(i, color1)  # set first pixel with color1 starting at the latest pixel
    
    # set all pixel before with the same color 1
    for j in range(i-1, i-countPixelColor1, -1): 
      strip.setPixelColor(j, color1)
    
    # now set all pixels before colored1 pixels with color2
    # (for the first loop, it makes no sence, because there is no pixel before position 0,
    # but after the first loop, we now can switch the first pixel from color1 to color2
    strip.setPixelColor(i-countPixelColor1, color2) 
    strip.show()  # activate now all pixels with configured colors
    time.sleep(1.0125) # wait some (animation) time

  for k in range(strip.numPixels()-countPixelColor1-1, strip.numPixels()):
    strip.setPixelColor(k, color2)
    strip.setPixelColor((strip.numPixels()-k-countPixelColor1)*-1, color1)
    strip.show()
    time.sleep(1.0125)


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
