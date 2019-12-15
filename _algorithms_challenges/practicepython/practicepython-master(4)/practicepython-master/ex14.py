#write a program that takes a list and returns new list that contains all the elements of first list without duplicates
import random

def remove_duplicates_set(inputlist):
	return [element for element in set(inputlist) ]

def remove_duplicates_for(inputlist):
	newlist = []
	for element in inputlist:
		if element not in newlist:
			newlist.append(element)
	return newlist

if __name__ == "__main__":
	inputlist = [1,1,2,3,4,5,5,6,7,8,13,15,10,20]
	print "The input list is "
	print inputlist 
	print "The output list using set list comprehension "
	print remove_duplicates_set(inputlist)
	print "The output list using for loop alone is "
	print remove_duplicates_for( inputlist)
