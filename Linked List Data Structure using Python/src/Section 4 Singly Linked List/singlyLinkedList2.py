# Create nodes
# Create linked list
# Add nodes to linked list
# Print linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, newNode):
        # data = > Matthew, next => None
        temporaryNode = self.head # John
        self.head = newNode # Matthew
        self.head.next = temporaryNode
        del temporaryNode

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        # head => John -> Ben -> Matthew -> None
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


# Node => data, next
# firstNode.data => John, firstNode.next => None
firstNode = Node("John")
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node("Ben")
linkedList = LinkedList()
linkedList.insertEnd(secondNode)
thirdNode = Node("Matthew")
linkedList.insertHead(thirdNode)
linkedList.printList()

