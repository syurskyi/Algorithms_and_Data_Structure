from singlyLinkedList import Node, LinkedList

def swapNext(linkedList, previousNode, largestNode, nextNode):
    # 4->3->5->1 || 3->4->5->1 || 4->|1->5->None
    largestNode.next = nextNode.next
    nextNode.next = largestNode
    if largestNode is linkedList.head:
        linkedList.head = nextNode
        return
    previousNode.next =  nextNode

def sort(linkedList):
    # number of iterations = number of nodes - 1
    numberOfIterations = linkedList.listLength() - 1 # 3
    while numberOfIterations != 0: # 3, 2, 1
        largestNode = linkedList.head
        previousNode = None
        numberOfComparisons = numberOfIterations
        while numberOfComparisons != 0:
            if largestNode.data > largestNode.next.data:
                swapNext(linkedList, previousNode, largestNode, largestNode.next)
            else:
                previousNode = largestNode
                largestNode = largestNode.next
            numberOfComparisons -= 1

        numberOfIterations -= 1

nodeOne = Node(4)
nodeTwo = Node(3)
nodeThree = Node(5)
nodeFour = Node(1)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
sort(linkedList)
linkedList.printList()
