

from time import sleep as sleep
import sys
blue = "00274C"
maize = "FFCB05"
length = 20
cols = 30
delay = 0
i = True
j = 0
while True:
	print 0,
	print 15,
	if i:
		print 15,
	else:
		print 16,
	i = not i
	if j < 2:
		print blue
		j = j + 1
	elif j == 2:
		print maize
		j = j + 1
		if j == 3:
			j = 0
		
		


	sys.stdout.flush()
	sleep(100 / 1000)


#	print delay,
#	print 0,
	#print k,
	#print blue
	#sys.stdout.flush()
	#sleep(delay / 100) 
#
	#print delay,
	#print 0,
	#print l,
	#print maize
	#sys.stdout.flush()
	#sleep(delay / 100) 

#	i = (i + 1) % length
#	j = (j + 1) % length
#	k = (k + 3) % length
#	l = (l - 4) % length
