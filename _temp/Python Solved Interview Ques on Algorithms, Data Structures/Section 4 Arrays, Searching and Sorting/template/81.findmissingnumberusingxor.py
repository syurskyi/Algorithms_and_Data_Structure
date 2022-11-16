
___ findmissingnumberusingxor(myarray
        print "Given Array:", myarray
        #print "Len of the Array:", len(myarray)
	arraylen _ len(myarray)
	xorval _ 0
        #print "In the First loop"
	___ i __ range(1, arraylen + 2
                #print xorval,"^",i,"is",xorval^i
		xorval _ xorval ^ i
        #print "In the Next loop"
	___ i __ range(0, arraylen
                #print xorval,"^",myarray[i],"is",xorval^myarray[i]
		xorval _ xorval ^ myarray[i]
	print "Missing number is ", xorval
myarray _ [12, 8, 2, 1, 4, 6, 5, 7, 9, 3, 11]
findmissingnumberusingxor(myarray)
