a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

if len(a) >= len(b):
	minimum = b
	maximum = a
else:
	minimum = a
	maximum = b

for num in maximum:
	if num in minimum:
		c.append(num)

list(set(c))

print(c)