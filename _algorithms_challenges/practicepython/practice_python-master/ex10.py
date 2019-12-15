#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python. (Hint: Remember list comprehensions from Exercise 7).

Extra: Randomly generate two lists to test this
'''

def main():
	# Exercise 10 given lists for testing
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	l1 = common(a, b)
	print (l1)
	
	# Whole 'notha level: random lists (of random length)
	list1, list2 = generate_random_lists()
	l2 = common(list1, list2)
	print (l2)
	

def generate_random_lists():
	'''Generates two random lists, containing random ints in
	range (0,100] and with random lengths (0,25)'''
	
	import random
	i = 0
	lista = listb = []
	lista_len = random.randint(0, 25)
	random.seed()
	listb_len = random.randint(0, 25)
	while i < lista_len:
		lista.append(random.randint(0, 100))
		i += 1
	while i < listb_len:
		listb.append(random.randint(0, 100))
		i +=1 
	return lista, listb

def common(l1, l2):
	return list(set([elem for elem in l1 if elem in l2]))

if __name__ == "__main__":
	main()