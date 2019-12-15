# -*- coding: UTF-8 -*-
#this is to demonstrate slicing of a list

li = ["a" , "b", "mpilgrim" , "z", "example"]

#print the list
print "The original list \n",li

#slicing positive indice
#You can get a subset of a list, called a slice , by specifying two indices.
#The return value is a new list containing all the elements of the list, in order, starting with the first slice index (in this case li[1]), up to but not including the second slice index (in this case li[3]).
print "\nli[1:3] %s" %li[1:3] #first indice inclusive second indice exclusive


#Slicing works if one or both of the slice indices is negative. If it helps, you can think of it this way: reading the list from left to right, the first slice index specifies the first element you want, and
#the second slice index specifies the first element you don't want. The return value is everything in between.
print "\n li [1:-1] %s" % li[1:-1]

#lists are 0 based
print "\n li[0:3] %s" % li[0:3] #always the last indice is exluded


#trying out with shorthand notation

print "\n li[ :3] %s" %li[ :3] #0 to 3

print "\n li[3: ] %s" %li[3: ] # 3 to last

print "\n li[:] %s" %li[:] #all element. also copy list :)

#check for copy list

flag=(li[0:5]==li[:])
print flag
