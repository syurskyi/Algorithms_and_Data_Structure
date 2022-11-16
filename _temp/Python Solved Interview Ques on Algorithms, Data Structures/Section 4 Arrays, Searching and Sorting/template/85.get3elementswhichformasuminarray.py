___ getthreeelementswithsum(myarray, sum
        print "Sorted array:", myarray
        #print "length of array:", len(myarray)
	n _ l..(myarray)
	leftindex _ 0
	rightindex _ n - 1
	___ i __ range(0, n - 2
                #print "start for loop>>"
                #print "array:", myarray
		leftindex _ i + 1
		rightindex _ n - 1
                #print "i:", i
                #print "leftindex index:", leftindex
                #print "rightindex index:", rightindex 
		_____(leftindex < rightindex
                        #print "            start while loop >>>>>", myarray
                        #print "in while loop - i:", i 
                        #print "in while loop - leftindex index:", leftindex
                        #print "in while loop - rightindex index:", rightindex 
                        #print myarray[i],"+",myarray[leftindex],"+",myarray[rightindex],"actual sum is", myarray[i] + myarray[leftindex] + myarray[rightindex],"exp sum",sum
			#print myarray[i] + myarray[leftindex] + myarray[rightindex], sum
			__(myarray[i] + myarray[leftindex] + myarray[rightindex] __ sum
                                #print "the numbers forming the sum are found"
				print myarray[i], " + ", myarray[leftindex], " + ", myarray[rightindex], " = ", sum	
                                #print "exiting" 	
				r_ 1
			elif(myarray[i] + myarray[leftindex] + myarray[rightindex] < sum
				leftindex +_ 1
                                #print "sum is lesser then",sum,"so move leftindex index from",leftindex-1,"to",leftindex 
			____
				rightindex -_ 1
                                #print "sum is more then",sum,"so move rightindex index from",rightindex+1,"to",rightindex
                        #print "            <<<<< end while loop" 
                #print "<<end for loop"
	r_ 0
    
myarray _ [22, 6, 45, 40, 10, 18]
myarray.sort()
getthreeelementswithsum(myarray, 72)
