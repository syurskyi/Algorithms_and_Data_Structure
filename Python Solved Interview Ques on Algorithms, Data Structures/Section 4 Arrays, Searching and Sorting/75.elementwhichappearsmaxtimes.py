def elementwhichappearsmaxtimes(myarray):
	myarray.sort()
	print "sorted array:", myarray
	j = 0
	count = max = 1
	element = myarray[0]
	for i in range(1, len(myarray)):
                #print "in for loop:", myarray
                #print "comparing", myarray[i],"and", element   
		if (myarray[i] == element):
                        #print myarray[i],"and", element,"are same"   
			count += 1
                        #print myarray[i],"appeared", count,"times"
			if count > max:
                                #print count,"greater then", max
                                #print "maxrepeated element appearing till now", element   
				max = count
				maxRepeatedElement = element
		else:
			count = 1
			element = myarray[i]
			
	print maxRepeatedElement, "repeated for ", max

myarray = [4, 3, 1, 4, 3, 4, 3, 4, 4]
elementwhichappearsmaxtimes(myarray)
