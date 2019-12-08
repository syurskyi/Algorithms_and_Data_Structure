# Print the middle node of a Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = newNode

    def listLength(self):
        length = 0
        currentNode = self.head
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def printMiddle(self):
        length = self.listLength()
        if length != 0:
            if length == 1:
                print("Middle Node: ",self.head.data)
                return
            middlePosition = length // 2
            middleNode = self.head
            while middlePosition != 0:
                middleNode = middleNode.next
                middlePosition -= 1
            print("Middle Node: ",middleNode.data)

nodeOne = Node(1)
nodeTwo = Node(5)
nodeThree = Node(3)
nodeFour = Node(10)
nodeFive = Node(6)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
linkedList.printMiddle()
