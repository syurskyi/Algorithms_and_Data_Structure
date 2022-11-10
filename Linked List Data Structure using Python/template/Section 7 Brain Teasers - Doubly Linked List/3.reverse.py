from doublyLinkedList import Node, LinkedList

def reverse(linkedList):
    # (2->13->10->20->None | None<-2<-13<-10<-20) || (20->10->13->2->None | None<-20<-10<-13<-2)
    currentNode = linkedList.head
    while currentNode is not None:
        nextNode = currentNode.next # 13, 10, 20, None
        currentNode.next = currentNode.previous
        currentNode.previous = nextNode
        if currentNode.previous is None:
            linkedList.head = currentNode
        currentNode = nextNode

nodeOne = Node(2)
nodeTwo = Node(13)
nodeThree = Node(10)
nodeFour = Node(20)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
reverse(linkedList)
linkedList.printList()
