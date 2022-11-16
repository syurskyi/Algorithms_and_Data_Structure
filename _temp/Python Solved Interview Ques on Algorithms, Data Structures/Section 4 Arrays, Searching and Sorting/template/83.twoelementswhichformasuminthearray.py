
___ gettwoeleswhichformasum(myarray, Sum
        print "Find the sum",Sum,"in the Given array:",myarray
	tab _     # dict  # hash
        #print "Created tab:",tab
	#print "In the first loop"
	___ ele __ myarray:
		__ ele __ tab:
			tab[ele] +_ 1
		____ ele !_ " ":
			tab[ele] _ 1
		____
			tab[ele] _ 0
                #print "in loop: tab",tab,"for ele '",ele,"' in array ",myarray           

        #print "###################################" 
	#print "In the next loop"
	___ ele __ myarray:
                #print "Is",Sum,"-",ele,"found in",tab 
		__ Sum - ele __ tab:
			print ele, "+", Sum - ele, " = ", Sum		
	
myarray _ [10, 4, 45, 16, 12, 7]
myarray.sort()
gettwoeleswhichformasum(myarray, 26)
