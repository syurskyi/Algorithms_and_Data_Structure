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

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertAt(self, newNode, position):
        # head =>10->20->None || newNode => 15 -> None || position=>1
        if position < 0 or position > self.listLength():
            print("Invalid position")
            return
        if position is 0:
            self.insertHead(newNode)
            return
        currentNode = self.head # 10, 20
        currentPosition = 0 # 0, 1
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1


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
firstNode = Node(10)
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node(20)
linkedList = LinkedList()
linkedList.insertEnd(secondNode)
thirdNode = Node(15)
linkedList.insertAt(thirdNode, 10)
linkedList.printList()

