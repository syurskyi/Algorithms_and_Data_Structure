class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, newNode):
        if self.head is None:
            self.head = newNode
            self.head.previous = self.head
            return
        lastNode = self.head.previous
        newNode.previous = lastNode
        newNode.next = self.head
        self.head.previous = newNode
        self.head = newNode
        lastNode.next = self.head

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            self.head.previous = self.head
            return
        currentNode = self.head
        while currentNode.next is not self.head:
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.previous = currentNode
        newNode.next = self.head
        self.head.previous=newNode

    def deleteHead(self):
        if self.head is None:
            print("Empty list")
            return
        previousHead = self.head
        self.head = self.head.next
        self.head.previous = previousHead.previous
        previousHead.previous.next = self.head
        previousHead.previous = None
        previousHead.next = None

    def deleteEnd(self):
        if self.head is None:
            print("Empty List")
            return
        currentNode = self.head
        while True:
            if currentNode.next.next is self.head:
                break
            currentNode = currentNode.next
        self.head.previous = currentNode
        currentNode.next.previous = None
        currentNode.next.next = None
        currentNode.next = self.head

    def printList(self):
        if self.head is not None:
            currentNode = self.head
            while True:
                print(currentNode.data)
                currentNode = currentNode.next
                if currentNode is self.head:
                    break
            # Print previous of head node to verify the connection to last node
            print(currentNode.previous.data)

nodeOne = Node(10)
nodeTwo = Node(20)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertHead(nodeTwo)
linkedList.deleteEnd()
linkedList.printList()
