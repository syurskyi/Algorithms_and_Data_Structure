#this is to check the file read exception 


try:
	fsock = open("/filenotthere","r")
except IOError:
	print "the file does not exist.exception caught using try. exit gracefully"

print "this line will always be printed even if exception occurs or not.to show program execution continues"


fsock2 = open("/nottherefile","r")

print "this line will not print since exception has thrown above and program crashes"
