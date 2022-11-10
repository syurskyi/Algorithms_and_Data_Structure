from doublyLinkedList import Node, LinkedList

def divideByTwo(linkedList):
    # 2->13->5->10->15->None
    currentNode = linkedList.head.next
    while currentNode is not None:
        if currentNode.previous.data % 2 is not 0:
            currentNode.data = currentNode.data // 2
        currentNode = currentNode.next

nodeOne = Node(2)
nodeTwo = Node(13)
nodeThree = Node(10)
nodeFour = Node(20)
nodeFive = Node(15)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
divideByTwo(linkedList)
linkedList.printList()
