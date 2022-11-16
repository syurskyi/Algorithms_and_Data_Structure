#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Stack:
    ___ -  maxSize
        maxSize _ maxSize
        list _ []
    
    ___ __str__ 
        values _ list.reverse()
        values _ [str(x) ___ x __ list]
        r_ '\n'.join(values)
    
    # isEmpty
    ___ isEmpty 
        __ list == []:
            r_ True
        ____
            r_ False
    
    # isFull
    ___ isFull 
        __ len(list) == maxSize:
            r_ True
        ____
            r_ False
    
    #  Push
    ___ push value
        __ isFull(
            r_ "The stack is full"
        ____
            list.append(value)
            r_ "The element has been successfully inserted"
    # Pop
    ___ pop 
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            r_ list.pop()
    
    # peek
    ___ peek 
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            r_ list[len(list)-1]

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

    