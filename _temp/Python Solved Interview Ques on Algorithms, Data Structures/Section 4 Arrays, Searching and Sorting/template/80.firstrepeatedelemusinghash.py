
___ firstrepeatedeleinalistofrepeatednumbersusinghash(myarray
        print "Given array:",myarray
	tab _ {}  # hash
        #print "Created the tab:",tab
	max _ 0
	___ ele __ myarray:
                #print "start loop >>"
		__ ele __ tab and tab[ele] == 1:
			tab[ele] _ -2
                        #print "ele",ele,"exists", "tab[ele] was 1, assigning -2 ", tab
                        #print "in loop: tab",tab,"for ele'",ele,"' in array ",myarray
		elif ele __ tab and tab[ele] < 0:
			tab[ele] -_ 1
                        #print "ele",ele,"exists", "tab[ele] < 0 , subtracted -1 from it", tab
                        #print "in loop: tab",tab,"for ele'",ele,"' in array ",myarray
		elif ele !_ " ":
			tab[ele] _ 1
                        #print "newly adding ele",ele,"to tab", tab
                        #print "in loop: tab",tab,"for ele'",ele,"' in array ",myarray
		____
			tab[ele] _ 0
                #print "end loop <<" 

        #print "######################################################################################"

	___ ele __ myarray:
                #print "in second loop: tab",tab,"for ele'",ele,"' in array ",myarray
                #print "max is:",max  
		__ tab[ele] < max:
			max _ tab[ele]
			maxRepeatedElement _ ele
                        #print "in IF COND", tab[ele],ele,max

	print maxRepeatedElement, "repeated for ", abs(max), " times"
 
myarray _ [3, 10, 1, 1, 10, 1, 10, 5, 5]
firstrepeatedeleinalistofrepeatednumbersusinghash(myarray)
