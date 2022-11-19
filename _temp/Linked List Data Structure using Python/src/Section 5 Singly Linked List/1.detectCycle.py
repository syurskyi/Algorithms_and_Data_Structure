from singlyLinkedList import Node, LinkedList

c_ NewNode(Node
    ___ -  data
        super().- (data)
        isVisited _ F..

___ detectCycle(linkedList
    # John(True)->Ben(True)->Matthew(True)->Ben(True)
    currentNode _ linkedList.head
    currentNode.isVisited _ T..
    _____ T..:
        __ currentNode.n...isVisited __ T..:
            currentNode.n.. _ N..
            b..
        currentNode _ currentNode.n..
        currentNode.isVisited _ T..


# John->Ben->Matthew->Ben->(Matthew->Ben...)
nodeOne _ NewNode('John')
nodeTwo _ NewNode('Ben')
nodeThree _ NewNode('Matthew')
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
nodeThree.n.. _ nodeTwo
detectCycle(linkedList)
linkedList.printList()
