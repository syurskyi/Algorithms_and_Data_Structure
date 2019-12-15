
li = [1,2,3,4,5,1,1]


#print the original list
print "\n %s" % li

print li.remove(1) #returns none but removes first occurence

print li

print "\nagain repeat"
print li.remove(1) #returns none but removes first occurence

print li


print "\n use pop"
print li.pop() #returns the popped vale

print li


print "\nagain remove 1 should throw an exception"
print li.remove(1) # 1 does not exist in the list

print li
