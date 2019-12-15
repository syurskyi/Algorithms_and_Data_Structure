import random

random.seed()

a = [int(1000*random.random()) for i in range(100)]
b = [int(1000*random.random()) for i in range(1000)]
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