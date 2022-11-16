#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Stack of Plates

c_ PlateStack(
    ___ -  capacity
        capacity _ capacity
        stacks _ []
    
    ___ __str__ 
        r_ stacks
    
    ___ push item
        __ len(stacks) > 0 and (len(stacks[-1])) < capacity:
            stacks[-1].append(item)
        ____
            stacks.append([item])
    
    ___ pop 
        _____ len(stacks) and len(stacks[-1]) == 0:
            stacks.pop()
        __ len(stacks) == 0:
            r_ N..
        ____
            r_ stacks[-1].pop()
    
    ___ pop_at stackNumber
        __ len(stacks[stackNumber]) > 0:
            r_ stacks[stackNumber].pop()
        ____
            r_ N..


customStack_ PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.pop_at(1))