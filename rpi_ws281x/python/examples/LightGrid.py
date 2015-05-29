import time
import sys
from neopixel import *

class LightGrid:

    def __init__(self, height, width):
	LED_PIN = 18
	LED_FREQ_HZ = 800000
	LED_DMA = 5
	LED_BRIGHTNESS = 255
	LED_INVERT = False
        self.width = width
        self.height = height
	self.strand = Adafruit_NeoPixel(600, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	self.strand.begin()
	for i in range(600):
		self.strand.setPixelColor(i, Color(255, 140, 0))
	self.strand.show()

    def setPixel(self, t, row, col, color):
	if row % 2 == 1:
		col = 25 - col
	pix = self.width * row + col + row * 4 + 2

    def showGrid(self):
        self.strand.show()

    def setGrid(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.strands[i].setPixelColor(j, color)
