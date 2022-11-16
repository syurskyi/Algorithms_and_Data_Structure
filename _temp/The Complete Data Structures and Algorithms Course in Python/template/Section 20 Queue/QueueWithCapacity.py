#   Created by Elshad Karimov on 29/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Queue:
    ___ -  maxSize
        items _ maxSize * [N..]
        maxSize _ maxSize
        start _ -1
        top _ -1
    
    ___ __str__
        values _ [str(x) ___ x __ items]
        r_ ' '.join(values)
    
    ___ isFull
        __ top + 1 __ start:
            r_ T..
        ____ start __ 0 ___ top + 1 __ maxSize:
            r_ T..
        ____
            r_ F..
    
    ___ isEmpty
        __ top __ -1:
            r_ T..
        ____
            r_ F..
    
    ___ enqueue value
        __ isFull(
            r_ "The queue is full"
        ____
            __ top + 1 __ maxSize:
                top _ 0
            ____
                top +_ 1
                __ start __ -1:
                    start _ 0
            items[top] _ value
            r_ "The element is inserted at the end of Queue"
    
    ___ dequeue
        __ isEmpty(
            r_ "There is not any element in the Queue"
        ____
            firstElement _ items[start]
            start _ start
            __ start __ top:
                start _ -1
                top _ -1
            ____ start + 1 __ maxSize:
                start _ 0
            ____
                start +_ 1
            items[start] _ N..
            r_ firstElement
    
    ___ peek
        __ isEmpty(
            r_ "There is not any element in the Queue"
        ____
            r_ items[start]
    
    ___ delete
        items _ maxSize * [N..]
        top _ -1
        start _ -1






customQueue _ Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.delete()
print(customQueue)