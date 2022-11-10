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
            newNode.next = self.head
            return
        currentNode = self.head
        while(currentNode.next is not self.head):
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.next = self.head

    def insertHead(self, newNode):
        lastNode = self.head
        while(lastNode.next is not self.head):
            lastNode = lastNode.next
        previousHead = self.head
        self.head = newNode
        newNode.next = previousHead
        lastNode.next = self.head

    def deleteEnd(self):
        lastNode = self.head
        while(lastNode.next is not self.head):
            previousNode = lastNode
            lastNode = lastNode.next
        lastNode.next = None
        previousNode.next = self.head

    def deleteHead(self):
        lastNode = self.head
        while(lastNode.next is not self.head):
            lastNode = lastNode.next
        previousHead = self.head
        self.head = self.head.next
        lastNode.next = self.head
        previousHead.next = None

    def printList(self):
        currentNode = self.head
        while True:
            print(currentNode.data)
            currentNode = currentNode.next
            if currentNode is self.head:
                break
        print(currentNode.data)

nodeOne = Node(10)
nodeTwo = Node(20)
nodeThree = Node(30)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.deleteHead()
linkedList.printList()
