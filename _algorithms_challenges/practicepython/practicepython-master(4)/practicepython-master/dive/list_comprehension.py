#this is to demonstrate list comprehension
li = [1,9,8,4]

print [elem*2 for elem in li]

print "after comprehension print the original list should be unchanged\n %s " %li


#assign the value of comprehension to other list

compli = [elem*2 for elem in li]

print "\nThe newly stored list printed below %s \n" % compli
