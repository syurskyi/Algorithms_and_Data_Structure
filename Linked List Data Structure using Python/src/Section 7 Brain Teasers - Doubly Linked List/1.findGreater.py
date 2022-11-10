from doublyLinkedList import Node, LinkedList

def findGreater(linkedList):
    # 5->3->10->2->15->None
    length = linkedList.listLength() # 5
    if length > 3:
        middlePosition = length // 2 # 5 / 2 => 2
        currentNode = linkedList.head
        currentPosition = 0
        while True:
            if currentPosition == middlePosition:
                if currentNode.previous.data > currentNode.next.data:
                    print("Previous node has a greater value than next node")
                else:
                    print("Next node has a greater value than the previous node")
                break
            currentNode = currentNode.next
            currentPosition += 1
    else:
        print("Not enough nodes")

nodeOne = Node(5)
nodeTwo = Node(3)
nodeThree = Node(10)
nodeFour = Node(2)
nodeFive = Node(15)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
#linkedList.insertEnd(nodeThree)
#linkedList.insertEnd(nodeFour)
#linkedList.insertEnd(nodeFive)
linkedList.printList()
findGreater(linkedList)
