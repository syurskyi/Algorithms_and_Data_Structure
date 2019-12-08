
def seperateonezero(myarray):
	l = 0; r = len(myarray) - 1
        print "Given array:",myarray
        #print "left:",l
        #print "right:",r
	while(l < r):
                #print "start loop >>array:",myarray
                #print "left:",l
                #print "right:",r
		
                while(myarray[l] % 2 == 0 and l < r):
			l += 1
                #print "Found 1",myarray[l],"so move left from",l-1,"to",l

		while(myarray[r] % 2 == 1 and l < r):
			r -= 1
                #print "Found 0",myarray[r],"so move right from",r+1,"to",r

		if(l < r):
                        #print "IN IF CONDITION after two while loops:l < r",l,"<",r
                        #print "exchange myarray[left] with myarray[right]",myarray[l],myarray[r]
                        #print "exchange myarray[right] with myarray[left]",myarray[r],myarray[l]
			myarray[l], myarray[r] = myarray[r], myarray[l]
			l += 1
			r -= 1
                        #print "move left from",l-1,"to",l
                        #print "move right from",r+1,"to",r
                        #print "END IF CONDITION"
                #print "<<end loop"

myarray = [1,0,1,0,1,0]
seperateonezero(myarray)
print myarray
