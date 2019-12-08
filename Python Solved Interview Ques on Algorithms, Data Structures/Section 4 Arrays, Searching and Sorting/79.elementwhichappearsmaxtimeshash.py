
def elementwhichappearsmaxtime(myarray):
        print "Given array:",myarray
	tab = {}  # hash
        #print "Created tab:",tab
	max = 0
	for element in myarray:
		if element in tab:
			tab[element] += 1
		elif element != " ":
			tab[element] = 1
		else:
			tab[element] = 0
                #print "in loop: tab",tab,"for element'",element,"' in array ",myarray

	for element in myarray:
		if tab[element] > max:
			max = tab[element]
			maxRepeatedElement = element

	print maxRepeatedElement, "repeated for ", max, " times"
 
myarray = [4, 3, 1, 4, 3, 4, 3, 4, 4]
elementwhichappearsmaxtime(myarray)
