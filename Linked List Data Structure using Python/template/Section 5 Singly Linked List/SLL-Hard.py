# Delete nodes that have a greater value on the right side

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

    def deleteRight(self):
        currentNode = self.head
        while currentNode.next is not None:
            # Check if node on the right has a greater value
            if currentNode.next.data > currentNode.data:
                # If currentNode is the head node, delete it and make the new node as the head node
                if currentNode is self.head:
                    self.head = currentNode.next
                    currentNode.next = None
                    currentNode = self.head
                    continue
                # If currentNode is not head node, make the previous node point to next node and remove this node
                previousNode.next = currentNode.next
                currentNode.next = None
                currentNode = self.head
            else:
                # Advance to next node if the data on the right side is not greater than currentNode
                previousNode = currentNode
                currentNode = currentNode.next

    def printList(self):
        if self.head is None:
            print("Empty List")
            return
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next

nodeOne = Node(10)
nodeTwo = Node(5)
nodeThree = Node(6)
nodeFour = Node(2)
nodeFive = Node(3)
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
linkedList.deleteRight()
linkedList.printList()
