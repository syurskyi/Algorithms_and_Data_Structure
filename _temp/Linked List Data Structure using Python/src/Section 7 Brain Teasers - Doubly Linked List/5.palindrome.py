from doublyLinkedList import Node, LinkedList

___ palindrome(linkedList
    # L, E, V, E, L
    startPointer _ linkedList.head
    endPointer _ linkedList.head
    _____ endPointer.n.. __ n.. N..
        endPointer _ endPointer.n..
    _____ T..:
        __ startPointer __ endPointer:
            print("List is palindrome")
            r_
        __ startPointer.data __ endPointer.data:
            startPointer _ startPointer.n..
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
