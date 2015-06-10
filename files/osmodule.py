import os

try:
	f = open(os.environ["HOME"]+"/list.txt", "r")
	line = f.readline()
	print line
	f.close()
except IOError, e:
	print e