a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []


for element in a:
	if element < 5:
		print(element)

for element in a:
	if element < 5:
		b.append(element)

print(b)

print(list(element for element in a if element < 5))

print(list(filter(lambda x: x < 5,a)))