from singlyLinkedList import Node, LinkedList

class NewNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.isVisited = False

def detectCycle(linkedList):
    # John(True)->Ben(True)->Matthew(True)->Ben(True)
    currentNode = linkedList.head
    currentNode.isVisited = True
    while True:
        if currentNode.next.isVisited is True:
            currentNode.next = None
            break
        currentNode = currentNode.next
        currentNode.isVisited = True


# John->Ben->Matthew->Ben->(Matthew->Ben...)
nodeOne = NewNode('John')
nodeTwo = NewNode('Ben')
nodeThree = NewNode('Matthew')
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
nodeThree.next = nodeTwo
detectCycle(linkedList)
linkedList.printList()
