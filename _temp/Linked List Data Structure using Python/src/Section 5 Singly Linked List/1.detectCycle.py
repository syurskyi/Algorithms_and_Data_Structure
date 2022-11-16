from singlyLinkedList import Node, LinkedList

c_ NewNode(Node
    ___ -  data
        super().- (data)
        isVisited _ False

___ detectCycle(linkedList
    # John(True)->Ben(True)->Matthew(True)->Ben(True)
    currentNode _ linkedList.head
    currentNode.isVisited _ True
    _____ True:
        __ currentNode.next.isVisited __ True:
            currentNode.next _ N..
            break
        currentNode _ currentNode.next
        currentNode.isVisited _ True


# John->Ben->Matthew->Ben->(Matthew->Ben...)
nodeOne _ NewNode('John')
nodeTwo _ NewNode('Ben')
nodeThree _ NewNode('Matthew')
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
nodeThree.next _ nodeTwo
detectCycle(linkedList)
linkedList.printList()
