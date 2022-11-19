#   Created by Elshad Karimov on 27/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___ -  value_None
        value _ value
        n.. _ N..

c_ SLinkedList:
    ___ -  
        head _ N..
        tail _ N..
    ___ __iter__ 
        node _ head
        _____ node:
            yield node
            node _ node.n..
    # insert in Linked List
    ___ insertSLL value, location
        newNode _ ? ?
        __ head __ N..
            head _ newNode
            tail _ newNode
        ____
            __ location __ 0:
                ?.n.. _ head
                head _ newNode
            ____ location __ 1:
                ?.n.. _ N..
                tail.n.. _ newNode
                tail _ newNode
            ____
                tempNode _ head
                index _ 0
                _____ index < location - 1:
                    tempNode _ tempNode.n..
                    index +_ 1
                nextNode _ tempNode.n..
                tempNode.n.. _ newNode
                ?.n.. _ nextNode

    # Traverse Singly Linked List
    
    ___ traverseList 
        __ head __ N..
            print("The Singly Linked List does not exist")
        ____
            node _ head
            _____ node __ n.. N..
                print(node.value)
                node _ node.n..

 # Search for a node in Singly Linked List
    ___ searchSLL nodeValue
        __ head __ N..
            print("The Singly Linked List does not exist")
        ____
            node _ head
            _____ node __ n.. N..
                __ node.value __ nodeValue:
                    r_ node.value
                node _ node.n..
            r_ "The node does not exist in this SLL"
    # Delete a node from Singly Linked List
    ___ deleteNode location
        __ head __ N..
            r_ "The Singly Linked List does not exist"
        ____
            __ location __ 0:
                __ head __ tail:
                    head _ N..
                    tail _ N..
                ____
                    head _ head.n..
            ____ location __ 1:
                __ head __ tail:
                    head _ N..
                    tail _ N..
                ____
                    node _ head
                    _____ node __ n.. N..
                        __ node.n.. __ tail:
                            b..
                        node _ node.n..
                    node.n.. _ N..
                    tail _ node
            ____
                tempNode _ head
                index _ 0
                _____ index < location-1:
                    tempNode _ tempNode.n..
                    index +_ 1
                nextNode _ tempNode.n..
                tempNode.n.. _?.n..
    # Delete entire SLL
    ___ deleteEntireSLL 
        __ head __ N..
            print("SLL does not exist")
        ____
            head _ N..
            tail _ N..

singlyLinkedList _ SLinkedList()
singlyLinkedList.insertSLL(44,6)
print([node.value ___ node __ singlyLinkedList]) 

# node1 = Node(1)
# node2 = Node(2)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2

singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
print([node.value ___ node __ singlyLinkedList]) 
singlyLinkedList.insertSLL(5,3)
print([node.value ___ node __ singlyLinkedList]) 


