
___ elementwhichappearsmaxtime(myarray
        print "Given array:",myarray
	tab _ {}  # hash
        #print "Created tab:",tab
	max _ 0
	___ element __ myarray:
		__ element __ tab:
			tab[element] +_ 1
		elif element !_ " ":
			tab[element] _ 1
		____
			tab[element] _ 0
                #print "in loop: tab",tab,"for element'",element,"' in array ",myarray

	___ element __ myarray:
		__ tab[element] > max:
			max _ tab[element]
			maxRepeatedElement _ element

	print maxRepeatedElement, "repeated for ", max, " times"
 
myarray _ [4, 3, 1, 4, 3, 4, 3, 4, 4]
elementwhichappearsmaxtime(myarray)
