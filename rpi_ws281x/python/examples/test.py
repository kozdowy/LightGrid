from random import randint

width = 25
height = 20
colorMax = 16777215

def setpixel(delay, row, col, color):
	print " ".join([str(delay), str(row), str(col), str(color)])
i = 0
while (True):
	setpixel(1, randint(0, height), randint(0, width), hex(randint(0, colorMax))[2:].zfill(6))
	if i % 10 == 1:
		print "display"
	i = i + 1
