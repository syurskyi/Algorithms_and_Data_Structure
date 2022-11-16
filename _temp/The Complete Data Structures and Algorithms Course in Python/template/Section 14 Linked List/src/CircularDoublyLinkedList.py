#   Created by Elshad Karimov on 12/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___ -  value_None
        value _ value
        next _ N..
        prev _ N..

c_ CircularDoublyLinkedList:
    ___ -  
        head _ N..
        tail _ N..

    
    ___ __iter__ 
        node _ head
        _____ node:
            yield node
            node _ node.next
            __ node == tail.next:
                break
    
    #  Creation of Circular Doubly Linked List
    ___ createCDLL nodeValue
        newNode _ Node(nodeValue)
        head _ newNode
        tail _ newNode
        newNode.prev _ newNode
        newNode.next _ newNode
        r_ "The CDLL is created successfully"


    # Insertion Method in Circular Doubly Linked List
    ___ insertCDLL value, location
        __ head __ N..:
            r_ "The CDLL does not exist"
        ____
            newNode _ Node(value)
            __ location == 0:
                newNode.next _ head
                newNode.prev _ tail
                head.prev _ newNode
                head _ newNode
                tail.next _ newNode
            elif location == 1:
                newNode.next _ head
                newNode.prev _ tail
                head.prev _ newNode
                tail.next _ newNode
                tail _ newNode
            ____
                tempNode _ head
                index _ 0
                _____ index < location - 1:
                    tempNode _ tempNode.next
                    index +_ 1
                newNode.next _ tempNode.next
                newNode.prev _ tempNode
                newNode.next.prev _ newNode
                tempNode.next _ newNode
            r_ "The node has been successfully inserted"

    # Traversal of Circular Doubly Linked List
    ___ traversalCDLL 
        __ head __ N..:
            print("There is not any node for traversal")
        ____
            tempNode _ head
            _____ tempNode:
                print(tempNode.value)
                __ tempNode == tail:
                    break
                tempNode _ tempNode.next

    # Reverse traversal of Circular Doubly Linked List
    ___ reverseTraversalCDLL 
        __ head __ N..:
            print("There is not any node for reverse traversal")
        ____
            tempNode _ tail
            _____ tempNode:
                print(tempNode.value)
                __ tempNode == head:
                    break
                tempNode _ tempNode.prev
    
    # Search Circular Doubly Linked List
    ___ searchCDLL nodeValue
        __ head __ N..:
            r_ "There is not any node in CDLL"
        ____
            tempNode _ head
            _____ tempNode:
                __ tempNode.value == nodeValue:
                    r_ tempNode.value
                __ tempNode == tail:
                    r_ "The value does not exist in CDLL"
                tempNode _ tempNode.next
    
    # Delete a node from Circular Doubly Linked List
    ___ deleteNode location
        __ head __ N..:
            print("There is not any node to delete")
        ____
            __ location == 0:
                __ head == tail:
                    head.prev _ N..
                    head.next _ N..
                    head _ N..
                    tail _ N..
                ____
                    head _ head.next
                    head.prev _ tail
                    tail.next _ head
            elif location == 1:
                __ head == tail:
                    head.prev _ N..
                    head.next _ N..
                    head _ N..
                    tail _ N..
                ____
                    tail _ tail.prev
                    tail.next _ head
                    head.prev _ tail
            ____
                curNode _ head
                index _ 0
                _____ index < location - 1:
                    curNode _ curNode.next
                    index +_ 1
                curNode.next _ curNode.next.next
                curNode.next.prev _ curNode
            print("The node has been successfully deleted")
    
    # Delete entire Circular Doubly Linked List
    ___ deleteCDLL 
        __ head __ N..:
            print("There is not any element to delete")
        ____
            tail.next _ N..
            tempNode _ head
            _____ tempNode:
                tempNode.prev _ N..
                tempNode _ tempNode.next
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




    
