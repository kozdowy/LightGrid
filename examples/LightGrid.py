import time
import sys
from neopixel import *

class LightGrid:

    def __init__(self, width, height):
	LED_PIN = 18
	LED_FREQ_HZ = 800000
	LED_DMA = 5
	LED_BRIGHTNESS = 16
	LED_INVERT = False
        self.width = width
        self.height = height
	#print "height,width: "
	#print self.height,
	#print ",",
	#print self.width
#        self.strands = range(height)
#        for i in range(height):
#            self.strands[i] = Adafruit_NeoPixel(height, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
#            self.strands[i].begin()
	self.strand = Adafruit_NeoPixel(self.height * self.width, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	self.strand.begin()
	#print "strand is now ",
	#print self.strand.numPixels()

    def setPixel(self, t, row, col, color):
	pix = self.width * row + col
    	#print "setting pixel: ",
	#print pix
        self.strand.setPixelColor(pix, color)
	#print "set the pixel"
        self.strand.show()
	#print "shown the pixel"
	time.sleep(t / 1000)

    #def setGrid(self, grid):
        #for i in range(len(grid)):
            #for j in range(len(grid[0])):
                #self.strands[i].setPixelColor(j, color)

row = 1
col = 16
lights = LightGrid(row, col)



while True:
    line = sys.stdin.readline()
    #t = time.time()
    try:
	    lineSplit = line.split(" ")
	    r = int(lineSplit[3][0:2], 16)
	    g = int(lineSplit[3][2:4], 16)
	    b = int(lineSplit[3][4:6], 16)
	    #print "setting pixel " + lineSplit[1] + "," + lineSplit[2] + " to " + lineSplit[3] + " and waiting " + lineSplit[0]
	    lights.setPixel(int(lineSplit[0]), int(lineSplit[1]), int(lineSplit[2]), Color(r, g, b))
	    #print time.time() - t
    except:
    	    print "bad input"
