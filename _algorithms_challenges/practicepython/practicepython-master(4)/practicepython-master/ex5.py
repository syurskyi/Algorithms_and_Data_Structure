#take two lists as input and make a list that conatins only common elements between these two lists
import random

#my custom function
def findcommon( shortlist, longlist ):
        newlist = []
        for element in shortlist:
                if element in longlist:
                        newlist.append(element)
        return list(set(newlist))




#main program
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



shortlist = a
result = []
if len(a) < len (b):
	shortlist = a
	result = findcommon ( a, b )
else:
	shortlist = b
	result = findcommon ( b, a )

print result



#also we can do in a one liner like this

print {element for element in a and b if element in a and b }


#additional to generate two lists randomly and check 

#creates a list using random module. sample function creates the sample of 1000 and randint function picks a number between the mentioned range
list1 = random.sample(range(1000), random.randint(1,100))
list2 = random.sample(range(1000), random.randint(1,100))
print list1
print list2

#printing it in one line using list compreshension
print {element for element in list1 and list2 if element in list1 and list2}




