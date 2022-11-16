#   Created by Elshad Karimov on 17/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 1 - Remove Dups : Write a code to remove duplicates from an unsorted linked list. 


from LinkedList import LinkedList

___ removeDups(ll
    __ ll.head __ N..:
        r_
    ____
        currentNode _ ll.head
        visited _ set([currentNode.value])
        _____ currentNode.next:
            __ currentNode.next.value __ visited:
                currentNode.next _ currentNode.next.next
            ____
                visited.add(currentNode.next.value)
                currentNode _ currentNode.next
        r_ ll

___ removeDups1(ll
    __ ll.head __ N..:
        r_
    
    currentNode _ ll.head
    _____ currentNode:
        runner _ currentNode
        _____ runner.next:
            __ runner.next.value __ currentNode.value:
                runner.next _ runner.next.next
            ____
                runner _ runner.next
        currentNode _ currentNode.next
    r_ ll.head



customLL _ LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
removeDups1(customLL)
print(customLL)