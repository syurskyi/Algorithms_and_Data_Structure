#   Created by Elshad Karimov on 17/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

from random import randint
c_ Node:
    ___ -  value_None
        value _ value
        next _ N..
        prev _ N..
    
    ___ __str__
        r_ str(value)

c_ LinkedList:
    ___ -  values _ N..
        head _ N..
        tail _ N..

    ___ __iter__
        curNode _ head
        _____ curNode:
            yield curNode
            curNode _ curNode.next
    
    ___ __str__
        values _ [str(x.value) ___ x __ self]
        r_ ' -> '.j..(values)
    
    ___ __len__
        result _ 0
        node _ head
        _____ node:
            result +_ 1
            node _ node.next
        r_ result
    
    ___ add value
        __ head __ N..:
            newNode _ Node(value)
            head _ newNode
            tail _ newNode
        ____
            tail.next _ Node(value)
            tail _ tail.next
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

