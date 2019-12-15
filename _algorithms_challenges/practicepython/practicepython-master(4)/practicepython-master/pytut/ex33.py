

list=[]

i=0

while i<6:
    list.append(i)
    i+=1
    print "Numbers now: ", list
    print "At the bottom i is %d" % i

print "printing the elements"
for element in list:
    print element
