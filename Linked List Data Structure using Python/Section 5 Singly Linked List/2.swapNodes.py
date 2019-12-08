from singlyLinkedList import Node, LinkedList

def swapNodes(linkedList, dataOne, dataTwo):
    # 4->3->5->2->7->1 || 4->7->5->2->3->1
    # 4 -> previousFirst
    # 3 -> FirstNode
    # 2 -> previousSecond
    # 7 -> secondNode
    currentNode = linkedList.head
    previousFirst = None
    previousSecond = None
    while True:
        if currentNode.data == dataOne:
            firstNode = currentNode
            break
        previousFirst = currentNode
        currentNode = currentNode.next
    currentNode = linkedList.head
    while True:
        if currentNode.data == dataTwo:
            secondNode = currentNode
            break
        previousSecond = currentNode
        currentNode = currentNode.next
    # Changing pointers
    previousFirst.next = secondNode
    nextSecond = secondNode.next
    secondNode.next = firstNode.next
    previousSecond.next = firstNode
    firstNode.next = nextSecond

nodeOne = Node(4)
nodeTwo = Node(3)
nodeThree = Node(5)
nodeFour = Node(2)
nodeFive = Node(7)
nodeSix = Node(1)
linkedList = LinkedList()
#4->7->5->2->3->1
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
linkedList.insertEnd(nodeSix)
swapNodes(linkedList, 3, 7)
linkedList.printList()
