
def findmissingnumberusingxor(myarray):
        print "Given Array:", myarray
        #print "Len of the Array:", len(myarray)
	arraylen = len(myarray)
	xorval = 0
        #print "In the First loop"
	for i in range(1, arraylen + 2):
                #print xorval,"^",i,"is",xorval^i
		xorval = xorval ^ i
        #print "In the Next loop"
	for i in range(0, arraylen):
                #print xorval,"^",myarray[i],"is",xorval^myarray[i]
		xorval = xorval ^ myarray[i]
	print "Missing number is ", xorval
myarray = [12, 8, 2, 1, 4, 6, 5, 7, 9, 3, 11]
findmissingnumberusingxor(myarray)
