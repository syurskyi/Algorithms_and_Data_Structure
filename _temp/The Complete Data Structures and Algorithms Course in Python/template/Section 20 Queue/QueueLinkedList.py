#   Created by Elshad Karimov on 30/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


c_ Node:
    ___ -  value_None
        value _ value
        n.. _ N..
    
    ___ __str__ 
        r_ s..(value)

c_ LinkedList
    ___ -  
        head _ N..
        tail _ N..
    
    ___ __iter__ 
        curNode _ head
        _____ curNode:
            yield curNode
            curNode _ curNode.n..

c_ Queue:
    ___ -  
        linkedList _ LinkedList()
    
    ___ __str__ 
        values _ [s..(x) ___ x __ linkedList]
        r_ ' '.j..(values)
    
    ___ enqueue value
        newNode _ ? ?
        __ linkedList.head __ N..
            linkedList.head _ newNode
            linkedList.tail _ newNode
        ____
            linkedList.tail.n.. _ newNode
            linkedList.tail _ newNode
    
    ___ isEmpty 
        __ linkedList.head __ N..
            r_ T..
        ____
            r_ F..
    
    ___ dequeue 
        __ isEmpty(
            r_ "There is not any node in the Queue"
        ____
            tempNode _ linkedList.head
            __ linkedList.head __ linkedList.tail:
                linkedList.head _ N..
                linkedList.tail _ N..
            ____
                linkedList.head _ linkedList.head.n..
            r_ tempNode
    
    ___ peek 
        __ isEmpty(
            r_ "There is not any node in the Queue"
        ____
            r_ linkedList.head
    
    ___ delete 
        linkedList.head _ N..
        linkedList.tail _ N..




custQueue _ Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print(custQueue.peek())
print(custQueue)