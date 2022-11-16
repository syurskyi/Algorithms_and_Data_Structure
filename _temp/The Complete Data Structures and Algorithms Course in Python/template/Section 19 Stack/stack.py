#   Created by Elshad Karimov on 19/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ MultiStack:

    ___ -  stacksize
        numstacks _ 3
        array _ [0] * (stacksize * numstacks)
        sizes _ [0] * numstacks
        stacksize _ stacksize
        # print(self.array)
        # print(self.sizes)

    ___ Push item, stacknum
        __ IsFull(stacknum
            raise Exception('Stack is full')
        sizes[stacknum] +_ 1
        array[IndexOfTop(stacknum)] _ item

    ___ Pop stacknum
        __ IsEmpty(stacknum
            raise Exception('Stack is empty')
        value _ array[IndexOfTop(stacknum)]
        array[IndexOfTop(stacknum)] _ 0
        sizes[stacknum] -_ 1
        r_ value

    ___ Peek stacknum
        __ IsEmpty(stacknum
            raise Exception('Stack is empty')
        r_ array[IndexOfTop(stacknum)]

    ___ IsEmpty stacknum
        r_ sizes[stacknum] == 0

    ___ IsFull stacknum
        r_ sizes[stacknum] == stacksize

    ___ IndexOfTop stacknum
        offset _ stacknum * stacksize
        r_ offset + sizes[stacknum] - 1

stack _ MultiStack(1)

