#   Created by Elshad Karimov on 01/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___ -  value_None
        value _ value
        n.. _ N..

c_ CircularSinglyLinkedList:
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
            

    #  Creation of circular singly linked list
    ___ createCSLL nodeValue
        node _ Node(nodeValue)
        node.n.. _ node
        head _ node
        tail _ node
        r_ "The CSLL has been created"
    
    #  Insertion of a node in circular singly linked list

    ___ insertCSLL value, location
        __ head __ N..
            r_ "The head reference is None"
        ____
            newNode _ ? ?
            __ location __ 0:
                ?.n.. _ head
                head _ newNode
                tail.n.. _ newNode
            ____ location __ 1:
                ?.n.. _ tail.n..
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
            r_ "The node has been successfully inserted"
    
    # Traversal of a node in circular singly linked list
    ___ traversalCSLL 
        __ head __ N..
            print("There is not any element for traversal")
        ____
            tempNode _ head
            _____ tempNode:
                print(tempNode.value)
                tempNode _ tempNode.n..
                __ tempNode __ tail.n..:
                    b..
    
    # Searching for a node in circular singly linked list
    ___ searchCSLL nodeValue
        __ head __ N..
            r_ "There is not any node in this CSLL"
        ____
            tempNode _ head
            _____ tempNode:
                __ tempNode.value __ nodeValue:
                    r_ tempNode.value
                tempNode _ tempNode.n..
                __ tempNode __ tail.n..:
                    r_ "The node does not exist in this CSLL"

    # Delete  a node from circular singly linked list
    ___ deleteNode location
        __ head __ N..
            print("There is not any node in CSLL")
        ____
            __ location __ 0:
                __ head __ tail:
                    head.n.. _ N..
                    head _ N..
                    tail _ N..
                ____
                    head _ head.n..
                    tail.n.. _ head
            ____ location __ 1:
                __ head __ tail:
                    head.n.. _ N..
                    head _ N..
                    tail _ N..
                ____
                    node _ head
                    _____ node __ n.. N..
                        __ node.n.. __ tail:
                            b..
                        node _ node.n..
                    node.n.. _ head
                    tail _ node
            ____
                tempNode _ head
                index _ 0
                _____ index < location - 1:
                    tempNode _ tempNode.n..
                    index +_ 1
                nextNode _ tempNode.n..
                tempNode.n.. _?.n..
    
    # Delete entire circular sinlgy linked list
    ___ deleteEntireCSLL 
        head _ N..
        tail.n.. _ N..
        tail _ N..



circularSLL _ CircularSinglyLinkedList()
circularSLL.createCSLL(0)
circularSLL.insertCSLL(1,1)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)

print([node.value ___ node __ circularSLL]) 
circularSLL.deleteEntireCSLL()
print([node.value ___ node __ circularSLL]) 












