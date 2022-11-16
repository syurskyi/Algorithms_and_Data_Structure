#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Stack:
    ___ -  maxSize
        maxSize _ maxSize
        list _    # list
    
    ___ __str__ 
        values _ list.reverse()
        values _ [str(x) ___ x __ list]
        r_ '\n'.join(values)
    
    # isEmpty
    ___ isEmpty 
        __ list __    # list:
            r_ T..
        ____
            r_ F..
    
    # isFull
    ___ isFull 
        __ l..(list) __ maxSize:
            r_ T..
        ____
            r_ F..
    
    #  Push
    ___ push value
        __ isFull(
            r_ "The stack is full"
        ____
            list.a..(value)
            r_ "The element has been successfully inserted"
    # Pop
    ___ pop 
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            r_ list.p.. 
    
    # peek
    ___ peek 
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            r_ list[l..(list)-1]

    #  delete
    ___ delete 
        list _ N..
    

customStack _ Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

    