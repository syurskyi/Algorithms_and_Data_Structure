from doublyLinkedList import Node, LinkedList

___ palindrome(linkedList
    # L, E, V, E, L
    startPointer _ linkedList.head
    endPointer _ linkedList.head
    _____ endPointer.next __ n.. N..:
        endPointer _ endPointer.next
    _____ True:
        __ startPointer == endPointer:
            print("List is palindrome")
            r_
        __ startPointer.data == endPointer.data:
            startPointer _ startPointer.next
            endPointer _ endPointer.previous
        ____
            print("List is not palindrome")
            r_

nodeOne _ Node('I')
nodeTwo _ Node('N')
nodeThree _ Node('D')
nodeFour _ Node('E')
nodeFive _ Node('X')
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
linkedList.printList()
palindrome(linkedList)
