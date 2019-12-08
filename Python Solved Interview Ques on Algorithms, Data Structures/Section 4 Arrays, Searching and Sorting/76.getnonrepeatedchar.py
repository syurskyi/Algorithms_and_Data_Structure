
def getfirstnonrepeated(myarray):
        print "Given array:", myarray
	tab = {}  # hash
        #print "tab created:", tab
	for ele in myarray.lower():
		if ele in tab:
			tab[ele] += 1
		elif ele != " ":
			tab[ele] = 1
		else:
			tab[ele] = 0
                #print "in loop:",tab,"for","'",ele,"'","in",myarray

	for ele in myarray.lower():
		if tab[ele] == 1:
			print("the first non repeated character is: %s" % (ele))
			return ele

	return
 
getfirstnonrepeated("abccdef")
