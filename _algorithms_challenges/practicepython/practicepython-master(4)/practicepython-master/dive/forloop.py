#for loop in python

li = ['a','b','e','d','f']

for element in li:
	print element


print "\n".join(li)

print "\n"

#counter using range

for i in range(5):
	print i

import os
for k,v in os.environ.items():
	print "%s=%s"%(k,v)
