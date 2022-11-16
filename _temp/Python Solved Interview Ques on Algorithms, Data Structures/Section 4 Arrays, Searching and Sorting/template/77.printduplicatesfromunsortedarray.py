
___ checkdup(myarray
        print "given array:",myarray
	___ i __ range(0, l..(myarray)):
                #print "myarray[",i,"] is",myarray[i]
		__(myarray[abs(myarray[i])] < 0
			print("Duplicates present:", abs(myarray[i]))
                        #print "in for loop:", myarray 
                        #print "array element:", myarray[i]  
			r_
		____
			myarray[myarray[i]] _ -myarray[myarray[i]]
                #print ">> in for loop:" 
                #print "array element:", myarray[i],"index is", i  
	        #print "changes made for",i,"th element in array","myarray[",myarray[i],"] is",myarray[myarray[i]]
                __ (myarray[i] < 0
                   print "" 
                   #print "In python lists, if the index is negative, then, the index is taken from the right side"
                   #print "So, here, if it is -2, then from right, if the array length is 5, then 2nd element from right of the array is changed"
                   #print "array after modification:", myarray
		
	print("No duplicates present in given array.")

myarray _ [3, 5, 4, 2, 1, 3]
checkdup(myarray)
