#   Created by Elshad Karimov on 05/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___ -  value_None
        value _ value
        next _ N..
        prev _ N..

c_ DoublyLinkedList:
    ___ -
        head _ N..
        tail _ N..

    
    ___ __iter__
        node _ head
        _____ node:
            yield node
            node _ node.next
    
    #  Creation of Doubly Linked List
    ___ createDLL nodeValue
        node _ Node(nodeValue)
        node.prev _ N..
        node.next _ N..
        head _ node
        tail _ node
        r_ "The DLL is created Successfully"
    
    
    
    #  Insertion Method in Doubly Linked List
    ___ insertNode nodeValue, location
        __ head __ N..:
            print("The node cannot be inserted")
        ____
            newNode _ Node(nodeValue)
            __ location __ 0:
                newNode.prev _ N..
                newNode.next _ head
                head.prev _ newNode
                head _ newNode
            ____ location __ 1:
                newNode.next _ N..
                newNode.prev _ tail
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
    
    #  Traversal Method in Doubly Linked List
    ___ traverseDLL
        __ head __ N..:
            print("There is not any element to traverse")
        ____
            tempNode _ head
            _____ tempNode:
                print(tempNode.value)
                tempNode _ tempNode.next
    
    #  Reverse Traversal Method in Doubly Linked List
    ___ reverseTraversalDLL
        __ head __ N..:
            print("There is not any element to traverse")
        ____
            tempNode _ tail
            _____ tempNode:
                print(tempNode.value)
                tempNode _ tempNode.prev

    # Search Method in Doubly Linked List
    ___ searchDLL nodeValue
        __ head __ N..:
            r_ "There is not any element in the list"
        ____
            tempNode _ head
            _____ tempNode:
                __ tempNode.value __ nodeValue:
                    r_ tempNode.value
                tempNode _ tempNode.next
            r_ "The node does not exist in this list"

    # Delete a node from Doubly Linked List
    ___ deleteNodelocation
        __ head __ N..:
            print("There is not any element in DLL")
        ____
            __ location __ 0:
                __ head __ tail:
                    head _ N..
                    tail _ N..
                ____
                    head _ head.next
                    head.prev _ N..
            ____ location __ 1:
                __ head __ tail:
                    head _ N..
                    tail _ N..
                ____
                    tail _ tail.prev
                    tail.next _ N..
            ____
                curNode _ head
                index _ 0
                _____ index < location - 1:
                    curNode _ curNode.next
                    index +_ 1
                curNode.next _ curNode.next.next
                curNode.next.prev _ curNode
            print("The node has been successfully deleted")

    # Delete entire Doubly Linked List
    ___ deleteDLL
        __ head __ N..:
            print("There is not any node in DLL")
        ____
            tempNode _ head
            _____ tempNode:
                tempNode.prev _ N..
                tempNode _ tempNode.next
            head _ N..
            tail _ N..
            print("The DLL has been successfully deleted")
    


doubyLL _ DoublyLinkedList()
doubyLL.createDLL(5)
doubyLL.insertNode(0,0)
doubyLL.insertNode(2,1)
doubyLL.insertNode(6,2)
print([node.value ___ node __ doubyLL])
doubyLL.deleteDLL()
print([node.value ___ node __ doubyLL])



