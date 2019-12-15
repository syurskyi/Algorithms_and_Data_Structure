a = [1,1,2,3,5,8,13,21,34,55,89]

number = int(raw_input("Enter a number to check all numbers below that from the list we have> "))


#print all the elements in the above list that are less than user input
result_list=[]
for element in a:
	if element < number:
		result_list.append(element)

print result_list


#doing the above in one line
newlist = [element for element in a if element<number]

print newlist
