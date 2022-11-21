#   Created by Elshad Karimov on 30/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


c_ Node:
    ___ -  value_N..
        ? _ ?
        n.. _ N..
    
    ___ __str__ 
        r_ s..(value)

c_ LinkedList
    ___ -  
        h.. _ N..
        t.. _ N..
    
    

c_ Queue:
    ___ -  
        linkedList _ LinkedList()
    
    ___ __str__ 
        values _ [s..(x) ___ x __ linkedList]
        r_ ' '.j..(values)
    
    ___ enqueue value
        newNode _ ? ?
        __ linkedList.head __ N..
            linkedList.h.. _ ?
            linkedList.tail _ ?
        ____
            linkedList.?.n.. _ ?
            linkedList.tail _ ?
    
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
                linkedList.h.. _ N..
                linkedList.t.. _ N..
            ____
                linkedList.head _ linkedList.?.n..
            r_ tempNode
    
    ___ peek 
        __ isEmpty(
            r_ "There is not any node in the Queue"
        ____
            r_ linkedList.head
    
    ___ delete 
        linkedList.h.. _ N..
        linkedList.t.. _ N..




# custQueue = Queue()
# custQueue.enqueue(1)
# custQueue.enqueue(2)
# custQueue.enqueue(3)
# print(custQueue)
# print(custQueue.peek())
# print(custQueue)