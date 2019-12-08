
def checkdupsorting(myarray):
	myarray.sort()
        print myarray
	for i in range(0, len(myarray) - 1):
                #print "in for loop:", myarray
                #print "comparing", myarray[i],"and",myarray[i + 1]  
		if(myarray[i] == myarray[i + 1]):
			print("Duplicates present:", myarray[i])
			return
	print("There are No duplicates present in the given array.")

myarray = [3,4,5,6,7,8,7]
checkdupsorting(myarray)
