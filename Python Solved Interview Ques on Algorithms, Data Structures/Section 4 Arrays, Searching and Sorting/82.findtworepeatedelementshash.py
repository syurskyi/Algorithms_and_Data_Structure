
def findtworepeatedelesusinghash(myarray):
        print "Given array:", myarray
	tab = {}  # hash
        #print "Created tab:", tab
	for ele in myarray:
		if ele in tab:
			tab[ele] += 1
		elif ele != " ":
			tab[ele] = 1
		else:
			tab[ele] = 0
                #print "in loop: tab",tab,"for ele '",ele,"' in array ",myarray

	for ele in myarray:
                #print "repeated eles are:"
		if tab[ele] == 2:
			print ele
			
myarray = [3, 5, 7, 18, 12, 18, 12, 1, 19]
findtworepeatedelesusinghash(myarray)
