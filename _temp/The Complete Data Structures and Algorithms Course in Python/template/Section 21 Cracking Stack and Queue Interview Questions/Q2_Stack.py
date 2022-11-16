#   Created by Elshad Karimov on 04/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.
  
#   Create Stack with min method

c_ Node(
    ___ -  value_None, next _ N..
        value _ value
        next _ next
    
    ___ __str__ 
        string _ str(value)
        __ next:
            string +_ ',' + str(next)
        r_ string

c_ Stack(
    ___ -  
        top _ N..
        minNode _ N..
    
    ___ min 
        __ n.. minNode:
            r_ N..
        r_ minNode.value
    
    ___ push item
        __ minNode and (minNode.value < item
            minNode _ Node(value _ minNode.value, next_self.minNode)
        ____
            minNode _ Node(value _ item, next_self.minNode)
        top _ Node(value_item, next_self.top)
    
    ___ pop 
        __ n.. top:
            r_ N..
        minNode _ minNode.next
        item _ top.value
        top _ top.next
        r_ item

customStack _ Stack()
customStack.push(5)
print(customStack.min())
customStack.push(6)
print(customStack.min())
customStack.push(3)
print(customStack.min())
customStack.pop()
print(customStack.min())

