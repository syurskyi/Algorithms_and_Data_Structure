#   Created by Elshad Karimov on 19/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 5 - Intersection

____ LinkedList ______ LinkedList, Node

___ intersection(llA, llB
    __ llA.tail __ n.. llB.tail:
        r_ F..
    
    lenA _ l..(llA)
    lenB _ l..(llB)

    shorter _ llA __ lenA < lenB ____ llB
    longer _ llB __ lenA < lenB ____ llA

    diff _ l..(longer) - l..(shorter)
    longerNode _ longer.head
    shorterNode _ shorter.head

    ___ i __ r..(diff
        longerNode _ longerNode.n..
    
    _____ shorterNode __ n.. longerNode:
        shorterNode _ shorterNode.n..
        longerNode _ longerNode.n..
    
    r_ longerNode


# Helper addition method
___ addSameNode(llA, llB, value
    tempNode _ ? ?
    llA.tail.n.. _ tempNode
    llA.tail _ tempNode
    llB.tail.n.. _ tempNode
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




    
