#   Created by Elshad Karimov on 19/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 5 - Intersection

from LinkedList import LinkedList, Node

___ intersection(llA, llB
    __ llA.tail __ n.. llB.tail:
        r_ False
    
    lenA _ l..(llA)
    lenB _ l..(llB)

    shorter _ llA __ lenA < lenB else llB
    longer _ llB __ lenA < lenB else llA

    diff _ l..(longer) - l..(shorter)
    longerNode _ longer.head
    shorterNode _ shorter.head

    ___ i __ range(diff
        longerNode _ longerNode.next
    
    _____ shorterNode __ n.. longerNode:
        shorterNode _ shorterNode.next
        longerNode _ longerNode.next
    
    r_ longerNode


# Helper addition method
___ addSameNode(llA, llB, value
    tempNode _ Node(value)
    llA.tail.next _ tempNode
    llA.tail _ tempNode
    llB.tail.next _ tempNode
    llB.tail _ tempNode

llA _ LinkedList()
llA.generate(3,0, 10)

llB _ LinkedList()
llB.generate(4,0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(intersection(llA, llB))




    
