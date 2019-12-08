
def firstrepeatedeleinalistofrepeatednumbersusinghash(myarray):
        print "Given array:",myarray
	tab = {}  # hash
        #print "Created the tab:",tab
	max = 0
	for ele in myarray:
                #print "start loop >>"
		if ele in tab and tab[ele] == 1:
			tab[ele] = -2
                        #print "ele",ele,"exists", "tab[ele] was 1, assigning -2 ", tab
                        #print "in loop: tab",tab,"for ele'",ele,"' in array ",myarray
		elif ele in tab and tab[ele] < 0:
			tab[ele] -= 1			
                        #print "ele",ele,"exists", "tab[ele] < 0 , subtracted -1 from it", tab
                        #print "in loop: tab",tab,"for ele'",ele,"' in array ",myarray
		elif ele != " ":
			tab[ele] = 1
                        #print "newly adding ele",ele,"to tab", tab
                        #print "in loop: tab",tab,"for ele'",ele,"' in array ",myarray
		else:
			tab[ele] = 0
                #print "end loop <<" 

        #print "######################################################################################"

	for ele in myarray:
                #print "in second loop: tab",tab,"for ele'",ele,"' in array ",myarray
                #print "max is:",max  
		if tab[ele] < max:
			max = tab[ele]
			maxRepeatedElement = ele
                        #print "in IF COND", tab[ele],ele,max

	print maxRepeatedElement, "repeated for ", abs(max), " times"
 
myarray = [3, 10, 1, 1, 10, 1, 10, 5, 5]
firstrepeatedeleinalistofrepeatednumbersusinghash(myarray)
