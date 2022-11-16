#   Created by Elshad Karimov on 23/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

#  How to create a Tuple?

newTuple _ ('a', 'b', 'c', 'd', 'e')
newTuple1 _ tuple('abcde')

print(newTuple1)

# Access Tuple elements

print(newTuple[0]) 


#  Traverse through tuple

___ i __ newTuple:
    print(i)


___ index __ r..(l..(newTuple
    print(newTuple[index])


#  How to search for an element in Tuple?

print('a' __ newTuple)

___ searchInTuple(pTuple, element
    ___ i __ pTuple:
        __ i __ element:
            r_ pTuple.index(i)
    r_ 'The element does not exist'

print(searchInTuple(newTuple, 'a'))

# Tuple Operations / Functions
myTuple _ (1,4,3,2,5)
myTuple1 _ (1,2,6,9,8,7)

print(myTuple + myTuple1) 
print(myTuple * 4)      
print(2 __ myTuple1)

myTuple1.count(2)
myTuple1.index(2)





