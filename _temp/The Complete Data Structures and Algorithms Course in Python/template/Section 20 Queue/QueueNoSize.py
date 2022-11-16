#   Created by Elshad Karimov on 29/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Queue:
    ___ -  
        items _    # list
    
    ___ __str__ 
        values _ [str(x) ___ x __ items]
        r_ ' '.j..(values)
    
    ___ isEmpty 
        __ items __    # list:
            r_ T..
        ____
            r_ F..
    
    ___ enqueue value
        items.a..(value)
        r_ "The element is inserted at the end of Queue"
    
    ___ dequeue 
        __ isEmpty(
            r_ "The is not any element in the Queue"
        ____
            r_ items.pop(0)
    
    ___ peek 
        __ isEmpty(
            r_ "The is not any element in the Queue"
        ____
            r_ items[0]
    
    ___ delete 
        items _ N..




customQueue _ Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
customQueue.delete()
