#   Created by Elshad Karimov on 27/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___ -  value_None
        ? _ ?
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
    ___ traverseSLL
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
           r_ "The list does not exist"
        ____
            node _ head
            _____ node __ n.. N..
                __ node.value __ nodeValue:
                    r_ node.value
                node _ node.n..
            r_ "The value does not exist in this list"

    #  Delete a node from Singly Linked List
    ___ deleteNode location
        __ head __ N..
            print("The SLL does not exist")
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
                _____ index < location - 1:
                    tempNode _ tempNode.n..
                    index +_ 1
                nextNode _ tempNode.n..
                tempNode.n.. _?.n..
    # Delete entire SLL
    ___ deleteEntireSLL
        __ head __ N..
            print("The SLL does not exist")
        ____
            head _ N..
            tail _ N..


singlyLinkedList _ SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(0, 4)


# print([node.value for node in singlyLinkedList]) 
# singlyLinkedList.deleteEntireSLL()
# print([node.value for node in singlyLinkedList]) 






