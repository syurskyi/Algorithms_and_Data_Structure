
___ seperatoddevennumbers(myarray
	l _ 0; r _ len(myarray) - 1
        print "Given array:",myarray
        #print "left:",l
        #print "right:",r
	_____(l < r
                #print "start loop >>array:",myarray
                #print "left:",l
                #print "right:",r
		
                _____(myarray[l] % 2 == 0 and l < r
			l +_ 1
                #print "Found odd number",myarray[l],"so move left from",l-1,"to",l

		_____(myarray[r] % 2 == 1 and l < r
			r -_ 1
                #print "Found even number",myarray[r],"so move right from",r+1,"to",r

		__(l < r
                        #print "IN IF CONDITION after two while loops:l < r",l,"<",r
                        #print "exchange myarray[left] with myarray[right]",myarray[l],myarray[r]
                        #print "exchange myarray[right] with myarray[left]",myarray[r],myarray[l]
			myarray[l], myarray[r] _ myarray[r], myarray[l]
			l +_ 1
			r -_ 1
                        #print "move left from",l-1,"to",l
                        #print "move right from",r+1,"to",r
                        #print "END IF CONDITION"
                #print "<<end loop"

myarray _ [12, 23, 44, 89, 88, 90, 35]
seperatoddevennumbers(myarray)
print myarray
