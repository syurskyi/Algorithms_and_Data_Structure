#   Created by Elshad Karimov on 17/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

from random import randint
c_ Node:
    ___ -  value_None
        value _ value
        n.. _ N..
        p.. _ N..
    
    ___ __str__
        r_ s..(value)

c_ LinkedList
    ___ -  values _ N..
        head _ N..
        tail _ N..

    ___ __iter__
        curNode _ head
        _____ curNode:
            yield curNode
            curNode _ curNode.n..
    
    ___ __str__
        values _ [s..(x.value) ___ x __ self]
        r_ ' -> '.j..(values)
    
    ___ __len__
        result _ 0
        node _ head
        _____ node:
            result +_ 1
            node _ node.n..
        r_ result
    
    ___ add value
        __ head __ N..
            newNode _ ? ?
            head _ newNode
            tail _ newNode
        ____
            tail.n.. _ ? ?
            tail _ tail.n..
        r_ tail
    
    ___ generate n, min_value, max_value
        head _ N..
        tail _ N..
        ___ i __ r..(n
            add(randint(min_value,max_value))
        r_ self

# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(len(customLL))

