def getthreeelementswithsum(myarray, sum):
        print "Sorted array:", myarray
        #print "length of array:", len(myarray)
	n = len(myarray)
	leftindex = 0
	rightindex = n - 1
	for i in range(0, n - 2):
                #print "start for loop>>"
                #print "array:", myarray
		leftindex = i + 1
		rightindex = n - 1
                #print "i:", i
                #print "leftindex index:", leftindex
                #print "rightindex index:", rightindex 
		while(leftindex < rightindex):
                        #print "            start while loop >>>>>", myarray
                        #print "in while loop - i:", i 
                        #print "in while loop - leftindex index:", leftindex
                        #print "in while loop - rightindex index:", rightindex 
                        #print myarray[i],"+",myarray[leftindex],"+",myarray[rightindex],"actual sum is", myarray[i] + myarray[leftindex] + myarray[rightindex],"exp sum",sum
			#print myarray[i] + myarray[leftindex] + myarray[rightindex], sum
			if(myarray[i] + myarray[leftindex] + myarray[rightindex] == sum):
                                #print "the numbers forming the sum are found"
				print myarray[i], " + ", myarray[leftindex], " + ", myarray[rightindex], " = ", sum	
                                #print "exiting" 	
				return 1
			elif(myarray[i] + myarray[leftindex] + myarray[rightindex] < sum):
				leftindex += 1
                                #print "sum is lesser then",sum,"so move leftindex index from",leftindex-1,"to",leftindex 
			else:
				rightindex -= 1
                                #print "sum is more then",sum,"so move rightindex index from",rightindex+1,"to",rightindex
                        #print "            <<<<< end while loop" 
                #print "<<end for loop"
	return 0
    
myarray = [22, 6, 45, 40, 10, 18]
myarray.sort()
getthreeelementswithsum(myarray, 72)
