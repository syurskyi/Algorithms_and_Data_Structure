#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

#  Question 3 - Write code to partition a linked list around a value x, 
#               such that all nodes less than x come before all nodes greater than or equal to x. 

____ LinkedList ______ LinkedList

___ partition(ll, x
    curNode _ ll.head
    ll.tail _ ll.head

    _____ curNode:
        nextNode _ ?.n..
        ?.n.. _ N..
        __ curNode.value < x:
            ?.n.. _ ll.head
            ll.head _ curNode
        ____
            ll.tail.n.. _ curNode
            ll.tail _ curNode
        curNode _ nextNode
    
    __ ll.tail.n.. __ n.. N..
        ll.tail.n.. _ N..

customLL _ LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL, 30)
print(customLL)