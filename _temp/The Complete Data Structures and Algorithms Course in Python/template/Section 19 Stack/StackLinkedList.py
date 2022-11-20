#   Created by Elshad Karimov on 23/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___ -  value _ N..
        ? _ ?
        n.. _ N..

c_ LinkedList
    ___ -  
        head _ N..
    
    ___ __iter__ 
        curNode _ head
        _____ curNode:
            yield curNode
            curNode _ curNode.n..

c_ Stack:
    ___ -  
        LinkedList _ LinkedList()
    
    ___ __str__ 
        values _ [s..(x.value) ___ x __ LinkedList]
        r_ '\n'.j..(values)
    
    ___ isEmpty 
        __ LinkedList.head __ N..
            r_ T..
        ____
            r_ F..

    ___ push value
        node _ ? ?
        node.n.. _ LinkedList.head
        LinkedList.head _ node
    
    ___ pop 
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            nodeValue _ LinkedList.head.value
            LinkedList.head _ LinkedList.head.n..
            r_ nodeValue
    
    ___ peek 
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            nodeValue _ LinkedList.head.value
            r_ nodeValue
    
    ___ delete 
        LinkedList.head _ N..
    



customStack _ Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.peek())

