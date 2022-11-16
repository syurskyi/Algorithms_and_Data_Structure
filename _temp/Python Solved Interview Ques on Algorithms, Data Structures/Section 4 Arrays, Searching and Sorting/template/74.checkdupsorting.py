
___ checkdupsorting(myarray
	myarray.sort()
        print myarray
	___ i __ range(0, len(myarray) - 1
                #print "in for loop:", myarray
                #print "comparing", myarray[i],"and",myarray[i + 1]  
		__(myarray[i] == myarray[i + 1]
			print("Duplicates present:", myarray[i])
			r_
	print("There are No duplicates present in the given array.")

myarray _ [3,4,5,6,7,8,7]
checkdupsorting(myarray)
