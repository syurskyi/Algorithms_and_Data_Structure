#list is like arraylist in java

#A list is an ordered set of elements enclosed in square brackets
#A list can be used like a zero-based array. The first element of any non-empty list is always li[0]
#The last element of this five-element list is li[4], because lists are always zero-based.


li = ["a" , "b" , "mpilgrim" , "z" , "example"] #define a list

print li # print the list

print li[0] # print first element

print li [4] # print last element

#print li[5] #check out of bound should give error since index starts from 0 and there till 4. 5 t index not there


#accessing list from backward using negative indice. -1 means last element -2 second last etc

# A negative index accesses elements from the end of the list counting backwards. The last element of any non-empty list is always li[-1].
# If the negative index is confusing to you, think of it this way: li[-n] == li[len(li) - n]. So in this list, li[-3] == li[5 - 3] == li[2].

print li[-1]

print li[-3]

print li[-5]
#print li[-6]
