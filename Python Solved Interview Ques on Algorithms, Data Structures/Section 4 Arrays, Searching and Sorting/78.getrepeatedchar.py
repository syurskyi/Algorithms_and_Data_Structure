
def getrepeatedelement(A):
        print "given array:",A
	tab = {}  # hash
        #print "created a new tab:", tab
	for element in A.lower():
		if element in tab:
			tab[element] += 1
			print("the first repeated element is: %s" % (element))
                        #print "in loop: tab",tab,"for element '",element,"' in array ",A
			return element
		elif element != " ":
			tab[element] = 1
		else:
			tab[element] = 0
                #print "in loop: tab",tab,"for element '",element,"' in array ",A
	return

getrepeatedelement("abcdefd")
