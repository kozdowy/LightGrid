from neopixel import *
from LightGrid import LightGrid
row = 1
col = 30
print "creating grid"
lights = LightGrid(row, col)
print "created grid"
while 1==1:
    print "awaiting input"
    line = raw_input()
    lineSplit = line.split(" ")
    r = int(lineSplit[2][0:2], 16)
    g = int(lineSplit[2][2:4], 16)
    b = int(lineSplit[2][4:6], 16)
    setPixel(int(lineSplit[0]), int(lineSplit[1]), Color(r, g, b))
