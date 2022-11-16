#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

#  Question 3 - Write code to partition a linked list around a value x, 
#               such that all nodes less than x come before all nodes greater than or equal to x. 

from LinkedList import LinkedList

___ partition(ll, x
    curNode _ ll.head
    ll.tail _ ll.head

    _____ curNode:
        nextNode _ curNode.next
        curNode.next _ N..
        __ curNode.value < x:
            curNode.next _ ll.head
            ll.head _ curNode
        ____
            ll.tail.next _ curNode
            ll.tail _ curNode
        curNode _ nextNode
    
    __ ll.tail.next __ n.. N..:
        ll.tail.next _ N..

customLL _ LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL, 30)
print(customLL)