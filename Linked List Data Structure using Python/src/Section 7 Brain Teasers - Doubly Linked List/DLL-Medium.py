# Swap the first node and last node of a doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.previous = currentNode

    def swapHead(self):
        if self.head is None:
            print("Empty list")
            return
        # List has just 1 Node
        if self.head.next is None:
            return
        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        currentHead = self.head
        # Change previous pointer of head
        self.head.previous = lastNode.previous
        # Change previous pointer of next node of head
        self.head.next.previous = lastNode
        # Change next pointer of last node
        lastNode.next = self.head.next
        # Change next pointer of previous node of last node
        lastNode.previous.next = self.head
        # Change next pointer of head
        self.head.next = None
        # Change previous pointer of last node
        lastNode.previous = None
        # Make last node as head node
        self.head = lastNode


    def printList(self):
        if self.head is None:
            print("Empty list")
            return
        currentNode = self.head
        print("Printing from beginning")
        while True:
            print(currentNode.data)
            if currentNode.next is None:
                break
            currentNode = currentNode.next
        print("Printing from end")
        while True:
            print(currentNode.data)
            if currentNode.previous is None:
                break
            currentNode = currentNode.previous


nodeOne = Node(10)
nodeTwo = Node(30)
nodeThree = Node(15)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.swapHead()
linkedList.printList()
