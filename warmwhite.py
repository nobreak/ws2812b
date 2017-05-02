# rotation lamp for two colors
# Author: Philipp Homann 
#
import time
import colorsys

from neopixel import *
from thread import start_new_thread
from threading import Thread
from random import randint

# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels on stripe.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_TIME       = 0.055   # animation time (time from one pixel to the next
LED_START_PIXEL = 0     # where we want to start the animation on stripe
LED_END_PIXEL = 12      # where we want to end the animation on strip
LED_COLOR1         = Color(192,64,1)
COUNT_PIXEL_FIRST_COLOR = 6 # count how much pixels the fist color is long, second color count is the difference with LED_COUNT
LED_ROWS       = 5



# set all pixel aof stripe back to black
def reset(strip):
  for pixel in range(strip.numPixels()):
    strip.setPixelColor(pixel,Color(0,0,0))
  strip.show()

def setPixelBrightness(strip, pixel, brightness):
  # get color in rgb
  colorInt = strip.getPixelColor(pixel)
  blue =  colorInt & 255
  # for my strip i needed to switch green and red
  red = (colorInt >> 8) & 255
  green =   (colorInt >> 16) & 255

  # convert rgb to HSV
  r, g, b = [x/255.0 for x in red, green, blue]
  h, s, v = colorsys.rgb_to_hsv(r,g,b)
  
  # change v to the new brightness
  v = brightness/255.0

  # convert HSV back to RGB
  r, g, b = colorsys.hsv_to_rgb(h, s, v)
  r, g, b = [x*255.0 for x in r, g, b]

  # set new pixel color with RGB
  strip.setPixelColor(pixel, Color(int(r),int(g),int(b)))

def randomPixel(strip, color, countLED):

  reset(strip)
  while 1:
    pixel = randint(0,countLED)
    strip.setPixelColor(pixel, color)
    strip.show()
    time.sleep(2)

    for b in range(255,0,-1):
      setPixelBrightness(strip,pixel,b)
      strip.show()
      time.sleep(0.015)


def testDimming(strip, color):
  for p in range(0,60,1):
    strip.setPixelColor(p, Color(192,64,1))

#  setPixelBrightness(strip, 30,5)

  strip.show()
  time.sleep(20)



# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Color wipe animations.
                testDimming(strip, LED_COLOR1)
                #randomPixel(strip, LED_COLOR1, LED_COUNT)
