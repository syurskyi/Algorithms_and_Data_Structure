
___ getfirstoccurenceofanumusingbinsearch(myarray, value
	__ myarray __ N.. __ l..(myarray) __ 0:
	    r_ -1;
	h _ l..(myarray) - 1
        l _ 0
        m _ 0
        found _ -1;

        print "given sorted array:", myarray
        #print "len:", len(myarray)
        #print "high:", h
        #print "low:", l
        #print "mid:", m

        _____(1
            #print "start loop >>"
            #print "given array:", myarray
            #print "high:", h
            #print "low:", l
            __ (l > h
               #print "low",l,"greater then high",h,
               print "returning the",value,"found at position",found     
               r_ found
            m _ (l + h) / 2
            #print "mid:", m
            __ (myarray[m] __ value
               temp _ l
	       found _ m; l _ m + 1
               #print "element found at position:",m,"l moved from",temp,"to",l 
            __ (myarray[m] < value 
               temp_l
               l _ m + 1
               #print value,"more then",myarray[m],"at position",m,"low moved from",temp,"to",l
               
            __ (myarray[m] > value 
               temp_h
               h _ m - 1
               #print value,"less then",myarray[m],"at position",m,"high moved from",temp,"to",h
          
            #print "<< end loop"

        r_ m
	    
myarray _ [1,2,3,4,5,6,7,8,9,10,10]		
getfirstoccurenceofanumusingbinsearch(myarray, 10)
