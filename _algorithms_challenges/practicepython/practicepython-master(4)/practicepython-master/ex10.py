#print common elements in two lists without duplicates using list compreshension
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#create random numbers list x and y and find common
x = random.sample(range(0,100),20) # creates a sample of 20  random number from range 0 to 100 
print x 

y = random.sample(range(0,50),15) #creates a sample of 15 random number from range 0 to 50

print y

print [element for element in set(x) if element in y]

print "\nlist 1"
print a
print "\nlist 2"
print b
print "\ncommon elements in two lists without duplicates"
print [element for element in set(a)  if element in b]
