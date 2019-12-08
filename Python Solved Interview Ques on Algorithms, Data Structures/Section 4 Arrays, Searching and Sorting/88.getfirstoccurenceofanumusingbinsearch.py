
def getfirstoccurenceofanumusingbinsearch(myarray, value):
	if myarray == None or len(myarray) == 0:
	    return -1;
	h = len(myarray) - 1
        l = 0
        m = 0
        found = -1;

        print "given sorted array:", myarray
        #print "len:", len(myarray)
        #print "high:", h
        #print "low:", l
        #print "mid:", m

        while(1):
            #print "start loop >>"
            #print "given array:", myarray
            #print "high:", h
            #print "low:", l
            if (l > h):
               #print "low",l,"greater then high",h,
               print "returning the",value,"found at position",found     
               return found
            m = (l + h) / 2
            #print "mid:", m
            if (myarray[m] == value):
               temp = h
	       found = m; h = m - 1
               #print "element found at position:",m,"high moved from",temp,"to",h 
            if (myarray[m] < value): 
               temp=l
               l = m + 1
               #print value,"more then",myarray[m],"at position",m,"low moved from",temp,"to",l
               
            if (myarray[m] > value): 
               temp=h
               h = m - 1
               #print value,"less then",myarray[m],"at position",m,"high moved from",temp,"to",h
          
            #print "<< end loop"

        return m
	    
myarray = [1,2,3,4,5,6,7,8,9,10,10]		
getfirstoccurenceofanumusingbinsearch(myarray, 10)
