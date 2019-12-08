
def gettwoeleswhichformasum(myarray, Sum):
        print "Find the sum",Sum,"in the Given array:",myarray
	tab = {}  # hash
        #print "Created tab:",tab
	#print "In the first loop"
	for ele in myarray:
		if ele in tab:
			tab[ele] += 1
		elif ele != " ":
			tab[ele] = 1
		else:
			tab[ele] = 0		
                #print "in loop: tab",tab,"for ele '",ele,"' in array ",myarray           

        #print "###################################" 
	#print "In the next loop"
	for ele in myarray:
                #print "Is",Sum,"-",ele,"found in",tab 
		if Sum - ele in tab:
			print ele, "+", Sum - ele, " = ", Sum		
	
myarray = [10, 4, 45, 16, 12, 7]
myarray.sort()
gettwoeleswhichformasum(myarray, 26)
