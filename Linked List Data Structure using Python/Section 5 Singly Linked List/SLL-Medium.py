# In an integer linked list, count the number of nodes that are even and the number of nodes that are odd

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

    def countNodes(self):
        currentNode = self.head
        evenCount = 0
        oddCount = 0
        while currentNode is not None:
            if currentNode.data % 2 is 0:
                evenCount += 1
            else:
                oddCount += 1
            currentNode = currentNode.next
        print("Even Nodes: ",evenCount)
        print("Odd Nodes: ", oddCount)

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
linkedList.countNodes()
