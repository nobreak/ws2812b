# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.
def colorOnePixel(strip, color):
  for i in range(0,strip.numPixels()): # all pixel
    strip.setPixelColor(i, color)  # set pixel i to color
#    for j in range(i-1, 0,-1): # set all pixel behind pixel i to color zero
    strip.setPixelColor(i-1,0)
    strip.show()
    time.sleep(0.05)
  strip.setPixelColor(strip.numPixels()-1, 0)

def colorTwoPixel(strip, color):
  for i in range(1, strip.numPixels()):
    strip.setPixelColor(i, color)
    strip.setPixelColor(i-1, color)
    strip.setPixelColor(i-2, Color(255,0,0))
    strip.show()
    time.sleep(0.05)
  strip.setPixelColor(strip.numPixels()-1, Color(255,0,0))
  strip.setPixelColor(strip.numPixels()-2, Color(255,0,0))

def colorTwoPixelTwoColors(strip, color, color2):
  for i in range(1, strip.numPixels()):
    strip.setPixelColor(i, color)
    strip.setPixelColor(i-1, color)
    strip.setPixelColor(i-2, color2)
    strip.show()
    time.sleep(0.05)
  strip.setPixelColor(strip.numPixels()-1, color2)
  strip.setPixelColor(strip.numPixels()-2, color2)

def colorThreePixel(strip, color):
  for i in range(3, strip.numPixels()):
    strip.setPixelColor(i, color)
    strip.setPixelColor(i-1, color)
    strip.setPixelColor(i-2, color)
    strip.setPixelColor(i-3, 0) # set the pixel behind again to black
    strip.show()
    time.sleep(0.05)
  strip.setPixelColor(strip.numPixels()-1, 0)
  strip.setPixelColor(strip.numPixels()-2, 0)
  strip.setPixelColor(strip.numPixels()-3, 0)

def colorLampTwoColors(strip, color, color2, numPixel):
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
 # for l in range(0, numPixel):
 #   strip.setPixelColor(l, color)
 #   strip.show()
 #   time.sleep(0.015)

def colorLampOneColor(strip, color, numPixel):
  for i in range(numPixel-1, strip.numPixels()):
    strip.setPixelColor(i, color)
    for j in range(i-1, i-numPixel, -1):
      strip.setPixelColor(j, color)
    strip.setPixelColor(i-numPixel, Color(255,255,255))
    strip.show()
    time.sleep(0.115)
  for k in range(strip.numPixels(), strip.numPixels()-numPixel-1, -1):
    strip.setPixelColor(k, Color(255,255,255))




def colorHalfHalf(strip, color1, color2):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()/2):
                strip.setPixelColor(i, color1)
                strip.show()
        
        for j in range(strip.numPixels()/2,strip.numPixels()):
                strip.setPixelColor(j,color2)
                strip.show()


def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
	#	time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=500, iterations=1):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Color wipe animations.
#		colorWipe(strip, Color(255, 0, 0))  # Red wipe
#		colorWipe(strip, Color(0, 255, 0))  # Blue wipe
#		colorWipe(strip, Color(0, 0, 255))  # Green wipe
#                colorHalfHalf(strip, Color(0,0,255), Color(255,255,255))
#                colorOnePixel(strip, Color(0,0,155))
#                colorTwoPixel(strip, Color(0,0,255))
#                colorTwoPixelTwoColors(strip, Color(0,0,255), Color(0,255,0))
#                colorThreePixel(strip, Color(0,0,255))
#                colorLampOneColor(strip, Color(0,0,255), 6)
                colorLampTwoColors(strip, Color(0,255,0), Color(0,0,255), 30)
		# Theater chase animations.
#		theaterChase(strip, Color(127, 127, 127))  # White theater chase
#		theaterChase(strip, Color(127,   0,   0))  # Red theater chase
#		theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
		# Rainbow animations.
#		rainbow(strip)
#		rainbowCycle(strip)
#		theaterChaseRainbow(strip)
