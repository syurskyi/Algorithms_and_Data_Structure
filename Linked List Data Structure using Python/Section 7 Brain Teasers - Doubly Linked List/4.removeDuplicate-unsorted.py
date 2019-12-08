from doublyLinkedList import Node, LinkedList

def removeDuplicate(linkedList):
    # 13->5->13->2->13->None
    nodeCount = {}
    # {13: 1, 5:1, 2:1}
    currentNode = linkedList.head
    while True:
        if currentNode.data not in nodeCount.keys():
            nodeCount[currentNode.data] = 1
        else:
            nodeCount[currentNode.data] += 1
        if currentNode.next is None:
            while True:
                if currentNode.previous is None:
                    break
                previousNode = currentNode.previous
                if nodeCount[currentNode.data] > 1:
                    currentNode.previous.next = currentNode.next
                    if currentNode.next is not None:
                        currentNode.next.previous = currentNode.previous
                    currentNode.next = None
                    currentNode.previous = None
                    nodeCount[currentNode.data] -= 1
                currentNode = previousNode
            break    
        currentNode = currentNode.next


nodeOne = Node(13)
nodeTwo = Node(5)
nodeThree = Node(13)
nodeFour = Node(2)
nodeFive = Node(13)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
removeDuplicate(linkedList)
linkedList.printList()
