#simpler solution

import random

random.seed(5)

a = set([int(1000*random.random()) for i in range(100)])
b = set([int(1000*random.random()) for i in range(1000)])
c = []

c = a.intersection(b)

print(c)