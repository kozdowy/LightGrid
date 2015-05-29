from LightGrid import LightGrid
from neopixel import Color

row = 20
col = 26
lights = LightGrid(row, col)



while True:
    line = sys.stdin.readline()
    t = time.time()
    if line.strip() == 'q':
    	quit()
    if line.strip() == "display":
    	lights.showGrid()
    else:
	    try:
		    lineSplit = line.split(" ")
		    r = int(lineSplit[3][0:2], 16)
		    g = int(lineSplit[3][2:4], 16)
		    b = int(lineSplit[3][4:6], 16)
		    lights.setPixel(int(lineSplit[0]), int(lineSplit[1]), int(lineSplit[2]), Color(r, g, b))
	    except:
		    print "bad input"
