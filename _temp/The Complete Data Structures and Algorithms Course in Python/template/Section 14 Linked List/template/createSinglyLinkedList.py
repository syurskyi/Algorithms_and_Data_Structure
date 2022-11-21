#   Created by Elshad Karimov on 27/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ Node:
    ___ -  value_N..
        ? _ ?
        n.. _ N..

c_ SLinkedList:
    ___ -  
        h.. _ N..
        t.. _ N..
    ___ -i.. 
        node _ ?
        _____ ?
            y.. ?
            node _ ?.n..
    # insert in Linked List
    ___ insertSLL value, location
        newNode _ ? ?
        __ h.. __ N..
            h.. _ ?
            tail _ ?
        ____
            __ l.. __ 0
                ?.n.. _ ?
                h.. _ ?
            ____ l.. __ 1
                ?.n.. _ N..
                ?.n.. _ ?
                tail _ ?
            ____
                tempNode _ ?
                ? _ 0
                _____ ? < l.. - 1
                    t.. _ ?.n..
                    ? +_ 
                nextNode _ ?.n..
                ?.n.. _ newNode
                ?.n.. _ nextNode

    # Traverse Singly Linked List
    
    ___ traverseList 
        __ h.. __ N..
            print("The Singly Linked List does not exist")
        ____
            node _ ?
            _____ node __ n.. N..
                print(node.value)
                node _ ?.n..

 # Search for a node in Singly Linked List
    ___ searchSLL nodeValue
        __ h.. __ N..
            print("The Singly Linked List does not exist")
        ____
            node _ ?
            _____ node __ n.. N..
                __ node.value __ nodeValue:
                    r_ node.value
                node _ ?.n..
            r_ "The node does not exist in this SLL"
    # Delete a node from Singly Linked List
    ___ deleteNode location
        __ h.. __ N..
            r_ "The Singly Linked List does not exist"
        ____
            __ l.. __ 0
                __ ? __ t..
                    h.. _ N..
                    t.. _ N..
                ____
                    h.. _ ?.n..
            ____ l.. __ 1
                __ ? __ t..
                    h.. _ N..
                    t.. _ N..
                ____
                    node _ ?
                    _____ node __ n.. N..
                        __ node.n.. __ tail:
                            b..
                        node _ ?.n..
                    node.n.. _ N..
                    tail _ node
            ____
                tempNode _ ?
                ? _ 0
                _____ index < location-1:
                    t.. _ ?.n..
                    ? +_ 
                nextNode _ ?.n..
                ?.n.. _?.n..
    # Delete entire SLL
    ___ deleteEntireSLL 
        __ h.. __ N..
            print("SLL does not exist")
        ____
            h.. _ N..
            t.. _ N..

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


