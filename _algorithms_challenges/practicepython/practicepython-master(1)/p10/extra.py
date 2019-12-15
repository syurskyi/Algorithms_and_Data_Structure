import random

random.seed()

a = [int(1000*random.random()) for i in range(100)]
b = [int(1000*random.random()) for i in range(1000)]

if len(a) >= len(b):
	minimum = b
	maximum = a
else:
	minimum = a
	maximum = b

c = (element for element in set(maximum) if element in minimum)

print(list(c))
