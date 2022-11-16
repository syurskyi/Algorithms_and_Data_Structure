#   Created by Elshad Karimov on 23/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___ -  value _ N..
        value _ value
        next _ N..

c_ LinkedList:
    ___ -  
        head _ N..
    
    ___ __iter__ 
        curNode _ head
        _____ curNode:
            yield curNode
            curNode _ curNode.next

c_ Stack:
    ___ -  
        LinkedList _ LinkedList()
    
    ___ __str__ 
        values _ [str(x.value) ___ x __ LinkedList]
        r_ '\n'.join(values)
    
    ___ isEmpty 
        __ LinkedList.head __ N..:
            r_ True
        ____
            r_ False

    ___ push value
        node _ Node(value)
        node.next _ LinkedList.head
        LinkedList.head _ node
    
    ___ pop 
        __ isEmpty(
            r_ "There is not any element in the stack"
        ____
            nodeValue _ LinkedList.head.value
            LinkedList.head _ LinkedList.head.next
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

