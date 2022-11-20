
______ sys
___ gettwoelementsclosesttozero(myarray
        print "Given Array:", myarray
        #print "Length of the Array:", len(myarray) 
	arrayLen _ l..(myarray)
	myarray.s..
        #print "Array sorted:", myarray
	__(arrayLen < 2
		#print "Invalid Input"
		r_
	left _ 0
	right _ arrayLen - 1		
 	minimumLeft _ left
	minimumRight _ arrayLen - 1
	minimumSum _ sys.maxint
	_____(left < right
                #print "start loop>>"
                #print "array:", myarray
		sum _ myarray[left] + myarray[right];
                #print "Left index:", left
                #print "Right index:", right
                #print "Sum:", sum, "of", myarray[left],"+",myarray[right]
		__(abs(minimumSum) > abs(sum
			minimumSum _ sum
			minimumLeft _ left
			minimumRight _ right
                        #print "Until now, the two elements ", myarray[minimumLeft], myarray[minimumRight], "whose sum", sum,"is minimum"

		__ sum < 0:
			left +_ 1
                        #print "sum",sum,"is less then 0","move left index from",left-1,"to",left
		____ 
                      right -_ 1
                      #print "sum",sum,"is more then 0","move right index from",right+1,"to",right
                #print "<< end loop"
	print "Finally, the two elements whose sum is minimum are ", myarray[minimumLeft], myarray[minimumRight]

myarray _ [12, 70, -10, 50, -80, 85]
gettwoelementsclosesttozero(myarray)
