# rotation lamp for two colors
# Author: Philipp Homann 
#
import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels on stripe.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_TIME       = 0.015   # animation time (time from one pixel to the next
LED_START_PIXEL = 0     # where we want to start the animation on stripe
LED_END_PIXEL = 30      # where we want to end the animation on strip
LED_COLOR1         = Color(0,0,255)
LED_COLOR2         = Color(0,255,0)
COUNT_PIXEL_FIRST_COLOR = 2 # count how much pixels the fist color is long, second color count is the difference with LED_COUNT


# starts from the left and fills the pixels with the given color starting at startPosition up to countPixelColor1
#
# strip - the connected stripe
# color - the color which is to use
# startPixel - the pixel on the stripe where we want to start
# countPixels - the count of pixel wich we want to fill with the color after the start pixel
# animationTime - the time we wait to set the next pixel with the color
def fillInAnimation(strip, color, startPixel, countPixels, animationTime):
  #print("fillInAnimation")
  for pixel in range(startPixel, startPixel+countPixels, +1):
          strip.setPixelColor(pixel,color)
          strip.show()
          time.sleep(animationTime)


# move a collection of pixel to the right, all nomore used pixels on the left will be filled with color2
#
# strip - the connected stripe
# color1 - the color1 which is to use
# color2 - the color2 which is to use
# startPixelAnimation - the pixel on the stripe where we want to start
# startPixel - the start pixel on the strip where the animation could be - beginning at 0
# endPixel - the end pixel on the strip where the animation could be - beginning at 0
# animationTime - the time we wait to set the next pixel with the color
def moveAnimation(strip, color1, color2, startPixelAnimation, startPixel, endPixel, animationTime):
  #print("moveAnimation")
  for pixel in range(startPixelAnimation,endPixel, +1):
        strip.setPixelColor(pixel, color1)
        #print("Pixel: " + str(pixel) + " StartPixelAnimation:" + str(startPixelAnimation) + " StartPixel: " + str(startPixel) + " EndPixel:" + str(endPixel) + " Color2 Pixel:" + str(pixel - startPixelAnimation + startPixel)) 
        strip.setPixelColor(pixel-startPixelAnimation + startPixel ,color2)
        strip.show()
        time.sleep(animationTime)


# when the pixel collection of color1 reaches the end, we animate pixel by pixel again from the start (left side)
#
# strip - the connected stripe
# color1 - the color1 which is to use
# color2 - the color2 which is to use
# startPixel - the start pixel on the strip where the animation could be - beginning at 0
# endPixel - the end pixel on the strip where the animation could be - beginning at 0
# animationTime - the time we wait to set the next pixel with the color
def lineBreakAnimation(strip, color1, color2, countPixel, startPixel, endPixel, animationTime):
  #print("lineBreakAnimation")
  for pixel in range(endPixel-countPixel, endPixel):
        strip.setPixelColor(pixel, color2)
        #print("Pixel:" + str(pixel) + " EndPixel: " + str(endPixel) + " CountPixel: " + str(countPixel)) + " newPixel: " + str((endPixel-pixel-countPixel)*-1)
        strip.setPixelColor((endPixel-pixel-countPixel)*-1+startPixel, color1)
        strip.show()
        time.sleep(animationTime)


# set all pixel aof stripe back to black
def reset(strip):
  for pixel in range(strip.numPixels()):
    strip.setPixelColor(pixel,Color(0,0,0))
  strip.show()


# strip - the strip object a connected strip
# color1 - first color
# color2 - second color
# countPixelColor1 - count of pixels for color1, the count of pixels for color 2 will be calculated by LED_COUNT. Should be smaller than LED_COUNT
# timeValue - time to switch to the next pixel
# startPixel - the start pixel on the strip where the animation could be - beginning at 0
# endPixel - the end pixel on the strip where the animation could be - beginning at 0
def twoColorRotationLampMatrix(strip, color1, color2, countPixelColor1, timeValue, startPixel, endPixel):
   f = 1
   # loop for all needed pixels
   while 1: # endless loop	
      # fill the first pixels up to countPixelColor1
      # but only one time (f)
     while f == 1: 
        fillInAnimation(strip, color1, startPixel, countPixelColor1, timeValue)
        f = f+1

     # now move the first color to the right and add the second color on the left
     #endPixel = strip.numPixels()
     #endPixel = startPixel+6 #countLedPerRow
     moveAnimation(strip, color1, color2, startPixel+countPixelColor1, startPixel, endPixel, timeValue)
    
     # the following loop realized the animation of a coolection of pixels
     # with the same color over the end of the strip and starting again
     # at the beginning on the strip
     lineBreakAnimation(strip, color1, color2, countPixelColor1, startPixel, endPixel, timeValue)
 

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Color wipe animations.
                twoColorRotationLampMatrix(strip, LED_COLOR1, LED_COLOR2, COUNT_PIXEL_FIRST_COLOR, LED_TIME, LED_START_PIXEL, LED_END_PIXEL)
