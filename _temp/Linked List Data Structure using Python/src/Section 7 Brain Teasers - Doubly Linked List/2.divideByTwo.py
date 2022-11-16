from doublyLinkedList import Node, LinkedList

___ divideByTwo(linkedList
    # 2->13->5->10->15->None
    currentNode _ linkedList.head.next
    _____ currentNode __ n.. N..:
        __ currentNode.previous.data % 2 __ n.. 0:
            currentNode.data _ currentNode.data // 2
        currentNode _ currentNode.next

nodeOne _ Node(2)
nodeTwo _ Node(13)
nodeThree _ Node(10)
nodeFour _ Node(20)
nodeFive _ Node(15)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
divideByTwo(linkedList)
linkedList.printList()
