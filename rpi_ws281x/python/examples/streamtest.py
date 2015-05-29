from time import sleep as sleep
import sys
blue = "00274C"
maize = "FFCB05"
length = 30
cols = 10
i = 0
#j =  / 2
#k = 3 * length / 4
#l = length - 1
delay = 100
while True:
	print 100,
	print 0, 
	print i,
	print blue
	sys.stdout.flush()
	sleep(100 / 1000) 

	print 100,
	print 1,
	print i,
	print maize
	sys.stdout.flush()
	sleep(100 / 1000) 

	print 100,
	print 2, 
	print i,
	print blue
	sys.stdout.flush()
	sleep(100 / 1000) 

	print 100,
	print 3,
	print i,
	print maize
	sys.stdout.flush()
	sleep(100 / 1000) 

	print 100,
	print 4, 
	print i,
	print blue
	sys.stdout.flush()
	sleep(100 / 1000) 

	print 100,
	print 5,
	print i,
	print maize
	sys.stdout.flush()
	sleep(100 / 1000) 

	print 100,
	print 6, 
	print i,
	print blue
	sys.stdout.flush()
	sleep(100 / 1000) 

	print 100,
	print 7,
	print i,
	print maize
	sys.stdout.flush()
	sleep(100 / 1000) 

	print 100,
	print 8, 
	print i,
	print blue
	sys.stdout.flush()
	sleep(100 / 1000) 

	print 100,
	print 9,
	print i,
	print maize
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

	i = (i + 1) % length
#	j = (j + 1) % length
#	k = (k + 3) % length
#	l = (l - 4) % length
