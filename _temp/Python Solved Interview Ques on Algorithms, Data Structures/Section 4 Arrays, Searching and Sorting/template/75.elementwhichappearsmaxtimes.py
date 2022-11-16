___ elementwhichappearsmaxtimes(myarray
	myarray.sort()
	print "sorted array:", myarray
	j _ 0
	count _ max _ 1
	element _ myarray[0]
	___ i __ range(1, l..(myarray)):
                #print "in for loop:", myarray
                #print "comparing", myarray[i],"and", element   
		__ (myarray[i] __ element
                        #print myarray[i],"and", element,"are same"   
			count +_ 1
                        #print myarray[i],"appeared", count,"times"
			__ count > max:
                                #print count,"greater then", max
                                #print "maxrepeated element appearing till now", element   
				max _ count
				maxRepeatedElement _ element
		____
			count _ 1
			element _ myarray[i]
			
	print maxRepeatedElement, "repeated for ", max

myarray _ [4, 3, 1, 4, 3, 4, 3, 4, 4]
elementwhichappearsmaxtimes(myarray)
