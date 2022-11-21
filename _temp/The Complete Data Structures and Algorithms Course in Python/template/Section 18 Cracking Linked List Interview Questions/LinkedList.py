#   Created by Elshad Karimov on 17/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

____ random ______ randint
c_ Node:
    ___ -  value_N..
        ? _ ?
        n.. _ N..
        p.. _ N..
    
    ___ __str__
        r_ s..(value)

c_ LinkedList
    ___ -  values _ N..
        h.. _ N..
        t.. _ N..

    ___ -i..
        curNode _ ?
        _____ curNode:
            yield curNode
            c.. _ ?.n..
    
    ___ __str__
        values _ [s..(x.value) ___ x __ self]
        r_ ' -> '.j..(values)
    
    ___ __len__
        result _ 0
        node _ ?
        _____ ?
            result +_ 1
            node _ ?.n..
        r_ result
    
    ___ add value
        __ h.. __ N..
            newNode _ ? ?
            h.. _ ?
            tail _ ?
        ____
            tail.n.. _ ? ?
            tail _ tail.n..
        r_ tail
    
    ___ generate n, min_value, max_value
        h.. _ N..
        t.. _ N..
        ___ i __ r..(n
            add(randint(min_value,max_value))
        r_ self

# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(len(customLL))

