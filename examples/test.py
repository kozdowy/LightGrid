from random import randint

width = 20
height = 11
colorMax = 16777215

def setpixel(delay, row, col, color):
	print " ".join([str(delay), str(row), str(col), str(color)])

while (True):
	setpixel(1, randint(0, height), randint(0, width), hex(randint(0, colorMax))[2:].zfill(6))
