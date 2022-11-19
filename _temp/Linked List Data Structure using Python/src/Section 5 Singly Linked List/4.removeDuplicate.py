from singlyLinkedList import Node, LinkedList

___ removeDuplicate(linkedList
    # 1->2->3->3->5
    currentNode _ linkedList.head
    _____ T..:
        __ currentNode.data __ currentNode.n...data:
            duplicateNode _ currentNode.n..
            currentNode.n.. _ duplicateNode.n..
            duplicateNode.n.. _ N..
            b..
        currentNode _ currentNode.n..


nodeOne _ Node(1)
nodeTwo _ Node(2)
nodeThree _ Node(3)
nodeFour _ Node(3)
nodeFive _ Node(5)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
removeDuplicate(linkedList)
linkedList.printList()
