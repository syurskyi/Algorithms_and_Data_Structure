
___ getfirstnonrepeated(myarray
        print "Given array:", myarray
	tab _ {}  # hash
        #print "tab created:", tab
	___ ele __ myarray.lower(
		__ ele __ tab:
			tab[ele] +_ 1
		elif ele !_ " ":
			tab[ele] _ 1
		____
			tab[ele] _ 0
                #print "in loop:",tab,"for","'",ele,"'","in",myarray

	___ ele __ myarray.lower(
		__ tab[ele] == 1:
			print("the first non repeated character is: %s" % (ele))
			r_ ele

	r_
 
getfirstnonrepeated("abccdef")
