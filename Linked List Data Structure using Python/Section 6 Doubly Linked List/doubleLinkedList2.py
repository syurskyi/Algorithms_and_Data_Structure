class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, newNode):
        previousHead = self.head
        self.head = newNode
        self.head.next = previousHead
        previousHead.previous = self.head

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

nodeOne = Node('Joe')
nodeTwo = Node('Mary')
nodeThree = Node('Grace')
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertHead(nodeThree)
linkedList.printList()

