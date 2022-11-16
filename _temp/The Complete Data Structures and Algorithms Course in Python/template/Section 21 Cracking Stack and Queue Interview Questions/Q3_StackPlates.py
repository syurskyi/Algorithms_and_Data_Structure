#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Stack of Plates

c_ PlateStack(
    ___ -  capacity
        capacity _ capacity
        stacks _    # list
    
    ___ __str__ 
        r_ stacks
    
    ___ push item
        __ l..(stacks) > 0 ___ (l..(stacks[-1])) < capacity:
            stacks[-1].a..(item)
        ____
            stacks.a..([item])
    
    ___ pop 
        _____ l..(stacks) ___ l..(stacks[-1]) __ 0:
            stacks.p.. 
        __ l..(stacks) __ 0:
            r_ N..
        ____
            r_ stacks[-1].p.. 
    
    ___ pop_at stackNumber
        __ l..(stacks[stackNumber]) > 0:
            r_ stacks[stackNumber].p.. 
        ____
            r_ N..


customStack_ PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.pop_at(1))