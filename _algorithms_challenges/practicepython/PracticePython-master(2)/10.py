# List Overlap Comprehensions

# Given
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Common list: without duplicates, with one list comprehension
print list(set(i for i in a if i in b))
