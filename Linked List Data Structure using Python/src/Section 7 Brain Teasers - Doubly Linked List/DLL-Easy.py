# Delete a node with the given data in a doubly linked list

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

    def deleteNode(self, data):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == data:
                # head node deletion
                if currentNode is self.head:
                    self.head = currentNode.next
                    currentNode.next = None
                    if self.head is not None:
                        self.head.previous = None
                    return
                # last node deletion
                if currentNode.next is None:
                    currentNode.previous.next = None
                    currentNode.previous = None
                    return
                # node in between two nodes
                currentNode.next.previous = currentNode.previous
                currentNode.previous.next = currentNode.next
                currentNode.next = None
                currentNode.previous = None
                return
            currentNode = currentNode.next
        print("Data not found")

    def printList(self):
        if self.head is None:
            print("Empty list")
            return
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next

nodeOne = Node(10)
nodeTwo = Node(30)
nodeThree = Node(15)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.deleteNode(30)
linkedList.printList()
