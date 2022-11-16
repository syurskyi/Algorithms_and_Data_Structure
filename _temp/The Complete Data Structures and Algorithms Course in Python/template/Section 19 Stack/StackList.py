#   Created by Elshad Karimov on 22/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

    
c_ Stack:
    ___ -
        list _    # list
    
    ___ __str__
        values _ list.reverse()
        values _ [str(x) ___ x __ list]
        r_ '\n'.j..(values)
    
    # isEmpty
    ___ isEmpty
        __ list __    # list:
            r_ T..
        ____
            r_ F..
    # push
    ___ push value
        list.a..(value)
        r_ "The element has been successfully inserted"

    # pop
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
    
    # delete
    ___ delete
        list _ N..




customStack _ Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())
print(customStack)
