class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        # 10->20->None
        length = 0
        currentNode = self.head
        while currentNode is not None:
            currentNode = currentNode.next
            length += 1
        return length

    def insertHead(self, newNode):
        previousHead = self.head
        self.head = newNode
        self.head.next = previousHead
        previousHead.previous = self.head

    def insertAt(self, newNode, position):
        # 10->30->20 || position +> 1
        if position < 0 or position > self.listLength():
            print("Invalid position")
        if position is self.listLength():
            self.insertEnd(newNode)
            return
        if position is 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                currentNode.previous.next = newNode
                newNode.previous = currentNode.previous
                newNode.next = currentNode
                currentNode.previous = newNode
                break
            currentNode = currentNode.next
            currentPosition += 1

    def insertEnd(self, newNode):
        # (head=> Joe->Mary->Grace->None || head=>None <-Joe<-Mary<-Grace
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while True:
            if currentNode.next is None:
                break
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.previous = currentNode

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        print("Printing from the beginning")
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            if currentNode.next is None:
                reverseTraversalNode = currentNode
            currentNode = currentNode.next
        print("Printing form end")
        while True:
            if reverseTraversalNode is None:
                break
            print(reverseTraversalNode.data)
            reverseTraversalNode = reverseTraversalNode.previous

nodeOne = Node(10)
nodeTwo = Node(20)
nodeThree = Node(30)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertAt(nodeThree, 2)
linkedList.printList()

