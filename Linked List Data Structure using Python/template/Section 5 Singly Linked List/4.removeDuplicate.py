from singlyLinkedList import Node, LinkedList

def removeDuplicate(linkedList):
    # 1->2->3->3->5
    currentNode = linkedList.head
    while True:
        if currentNode.data == currentNode.next.data:
            duplicateNode = currentNode.next
            currentNode.next = duplicateNode.next
            duplicateNode.next = None
            break
        currentNode = currentNode.next


nodeOne = Node(1)
nodeTwo = Node(2)
nodeThree = Node(3)
nodeFour = Node(3)
nodeFive = Node(5)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
removeDuplicate(linkedList)
linkedList.printList()
