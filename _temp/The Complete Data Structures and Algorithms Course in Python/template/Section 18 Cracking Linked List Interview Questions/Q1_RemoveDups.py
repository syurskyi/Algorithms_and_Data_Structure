#   Created by Elshad Karimov on 17/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 1 - Remove Dups : Write a code to remove duplicates from an unsorted linked list. 


____ LinkedList ______ LinkedList

___ removeDups(ll
    __ ll.head __ N..
        r_
    ____
        currentNode _ ll.head
        visited _ s..([currentNode.value])
        _____ currentNode.n..:
            __ currentNode.n...value __ visited:
                currentNode.n.. _ currentNode.n...next
            ____
                visited.add(currentNode.n...value)
                currentNode _ currentNode.n..
        r_ ll

___ removeDups1(ll
    __ ll.head __ N..
        r_
    
    currentNode _ ll.head
    _____ currentNode:
        runner _ currentNode
        _____ runner.n..:
            __ runner.n...value __ currentNode.value:
                runner.n.. _ runner.n...next
            ____
                runner _ runner.n..
        currentNode _ currentNode.n..
    r_ ll.head



customLL _ LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
removeDups1(customLL)
print(customLL)