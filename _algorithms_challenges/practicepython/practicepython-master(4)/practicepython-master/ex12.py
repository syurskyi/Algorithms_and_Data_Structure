# this pogram takes in a list and creates a new list of first and last elements alone


import random

original_list = random.sample(range(0,100),30)

print original_list


def first_and_last_element(original_list):

	new_list = []
	new_list.append(original_list[0])
	new_list.append(original_list[-1])
	return new_list


print "getting the first and last element of the list using a function"

print first_and_last_element(original_list)
