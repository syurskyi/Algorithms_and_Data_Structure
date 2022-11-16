#   Created by Elshad Karimov on 10/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Accessing/Traversing the list

shoppingList _ ['Milk', 'Cheese', 'Butter']

___ i __ range(l..(shoppingList)):
    shoppingList[i] _ shoppingList[i]+"+"
    # print(shoppingList[i])
empty _    # list
___ i __ empty:
    print("I am empty")


# Update/Insert - List 

myList _ [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)

myList.a..(55)

newList _ [11,12,13,14]
myList.extend(newList)
print(myList)


#  Searching for an element in the List
myList _  [10,20,30,40,50,60,70,80,90]

___ searchinList(list, value
    ___ i __ list:
        __ i __ value:
            r_ list.index(value)
    r_ 'The value does not exist in the list'

print(searchinList(myList, 100))


#  List operations / functions
total _ 0 
count _ 0
_____ (True
    inp _ input('Enter a number: ') 
    __ inp __ 'done': break
    value _ float(inp)
    total _ total + value
    count _ count + 1 
    average _ total / count
					
print('Average:', average)



numlist _ list() 
_____ (True
    inp _ input('Enter a number: ') 
    __ inp __ 'done': break
    value _ float(inp)
    numlist.a..(value)
					
average _ sum(numlist) / l..(numlist) 
print('Average:', average)
