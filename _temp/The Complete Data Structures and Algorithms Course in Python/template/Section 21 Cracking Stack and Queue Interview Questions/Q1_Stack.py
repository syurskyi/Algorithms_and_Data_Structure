#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Use a single list to implement three stacks.

c_ MultiStack:
    ___ -  stacksize
        numberstacks _ 3
        custList _ [0] * (stacksize * numberstacks)
        sizes _ [0] * numberstacks
        stacksize _ stacksize
    
    ___ isFull stacknum
        __ sizes[stacknum] == stacksize:
            r_ True
        ____
            r_ False
    
    ___ isEmpty stacknum
        __ sizes[stacknum] == 0:
            r_ True
        ____
            r_ False
    
    ___ indexOfTop stacknum
        offset _ stacknum * stacksize
        r_ offset + sizes[stacknum]- 1
    
    ___ push item, stacknum
        __ isFull(stacknum
            r_ "The stack is full"
        ____
            sizes[stacknum] +_ 1
            custList[indexOfTop(stacknum)] _ item
    
    ___ pop stacknum
        __ isEmpty(stacknum
            r_ "The stack is empty"
        ____
            value _ custList[indexOfTop(stacknum)]
            custList[indexOfTop(stacknum)] _ 0
            sizes[stacknum] -_ 1
            r_ value
    
    ___ peek stacknum
        __ isEmpty(stacknum
            r_ "The stack is empty"
        ____
            value _ custList[indexOfTop(stacknum)]
            r_ value


customStack _ MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack.pop(0))
        
