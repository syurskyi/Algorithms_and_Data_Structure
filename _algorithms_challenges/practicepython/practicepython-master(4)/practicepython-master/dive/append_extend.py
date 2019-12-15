li = ["a" , "b", "mpilgrim", "z", "example"]

#print the list
print "original list %s" %li

li.append("new")

print "\nafter appending new element " ,li

#use insert to insert at specific index

li.insert(2,"new") #note the element new already exits but gets added

print "\n after inserting new elemnt at index 2 ",li

#use the extend.always extend will always conatain a list

li.extend([1,2,3])

print "\n after extending the list ", li


ali = ['a','b','c']
eli = ['a', 'b', 'c']

print ali
print eli


ali.append(['d','e','f'])
eli.extend(['d','e','f'])

print "\n appended list contains a list as last elemnt"
print ali

print "\n extended list contains new elements added to the existing list"
print eli

print "\n also note the difference in length between the two lists"
print "\n %d \n %d" %(len(ali),len(eli))


#searching a list using the index function

print "\n searching a list using the index function --returns first index only\n"
print li.index("new") #returns 1st index only

#returns true or false if we use <in>
print "no element check" in li

#throws exception if we use index for an element not existing
#print li.index("no element check")
