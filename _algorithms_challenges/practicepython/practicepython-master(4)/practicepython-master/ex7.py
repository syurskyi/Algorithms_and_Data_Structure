#given a list, use list compreshension to make a new list that 
#contains only the even numbers from the input list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


print "original list is %s \n"%a

print "even list"
print [element for element in a if element%2==0]
