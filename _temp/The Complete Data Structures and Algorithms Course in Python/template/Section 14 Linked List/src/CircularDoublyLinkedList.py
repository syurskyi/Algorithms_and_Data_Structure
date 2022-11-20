#   Created by Elshad Karimov on 12/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___ -  value_None
        ? _ ?
        n.. _ N..
        p.. _ N..

c_ CircularDoublyLinkedList:
    ___ -  
        head _ N..
        tail _ N..

    
    ___ __iter__ 
        node _ head
        _____ node:
            yield node
            node _ node.n..
            __ node __ tail.n..:
                b..
    
    #  Creation of Circular Doubly Linked List
    ___ createCDLL nodeValue
        newNode _ Node(nodeValue)
        head _ newNode
        tail _ newNode
        ?.p.. _ newNode
        ?.n.. _ newNode
        r_ "The CDLL is created successfully"


    # Insertion Method in Circular Doubly Linked List
    ___ insertCDLL value, location
        __ head __ N..
            r_ "The CDLL does not exist"
        ____
            newNode _ ? ?
            __ location __ 0:
                ?.n.. _ head
                ?.p.. _ tail
                head.p.. _ newNode
                head _ newNode
                tail.n.. _ newNode
            ____ location __ 1:
                ?.n.. _ head
                ?.p.. _ tail
                head.p.. _ newNode
                tail.n.. _ newNode
                tail _ newNode
            ____
                tempNode _ head
                index _ 0
                _____ index < location - 1:
                    tempNode _ tempNode.n..
                    index +_ 1
                ?.n.. _ tempNode.n..
                ?.p.. _ tempNode
                ?.n...prev _ newNode
                tempNode.n.. _ newNode
            r_ "The node has been successfully inserted"

    # Traversal of Circular Doubly Linked List
    ___ traversalCDLL 
        __ head __ N..
            print("There is not any node for traversal")
        ____
            tempNode _ head
            _____ tempNode:
                print(tempNode.value)
                __ tempNode __ tail:
                    b..
                tempNode _ tempNode.n..

    # Reverse traversal of Circular Doubly Linked List
    ___ reverseTraversalCDLL 
        __ head __ N..
            print("There is not any node for reverse traversal")
        ____
            tempNode _ tail
            _____ tempNode:
                print(tempNode.value)
                __ tempNode __ head:
                    b..
                tempNode _ tempNode.p..
    
    # Search Circular Doubly Linked List
    ___ searchCDLL nodeValue
        __ head __ N..
            r_ "There is not any node in CDLL"
        ____
            tempNode _ head
            _____ tempNode:
                __ tempNode.value __ nodeValue:
                    r_ tempNode.value
                __ tempNode __ tail:
                    r_ "The value does not exist in CDLL"
                tempNode _ tempNode.n..
    
    # Delete a node from Circular Doubly Linked List
    ___ deleteNode location
        __ head __ N..
            print("There is not any node to delete")
        ____
            __ location __ 0:
                __ head __ tail:
                    head.p.. _ N..
                    head.n.. _ N..
                    head _ N..
                    tail _ N..
                ____
                    head _ head.n..
                    head.p.. _ tail
                    tail.n.. _ head
            ____ location __ 1:
                __ head __ tail:
                    head.p.. _ N..
                    head.n.. _ N..
                    head _ N..
                    tail _ N..
                ____
                    tail _ tail.p..
                    tail.n.. _ head
                    head.p.. _ tail
            ____
                curNode _ head
                index _ 0
                _____ index < location - 1:
                    curNode _ curNode.n..
                    index +_ 1
                curNode.n.. _ curNode.n...next
                curNode.n...prev _ curNode
            print("The node has been successfully deleted")
    
    # Delete entire Circular Doubly Linked List
    ___ deleteCDLL 
        __ head __ N..
            print("There is not any element to delete")
        ____
            tail.n.. _ N..
            tempNode _ head
            _____ tempNode:
                tempNode.p.. _ N..
                tempNode _ tempNode.n..
            head _ N..
            tail _ N..
            print("The CDLL has been successfully deleted")
    


circularDLL _ CircularDoublyLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
print([node.value ___ node __ circularDLL])
circularDLL.deleteCDLL()
print([node.value ___ node __ circularDLL])




    
