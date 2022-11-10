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

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

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

    def deleteHead(self):
        if self.isListEmpty() is False:
            # head => 10 -> 15 -> 20 || 15->20->10-> None
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("Linked List is empty. Delete failed")

    def deleteAt(self, position):
        if position < 0 or position > self.listLength():
            print("Invalid position")
            return
        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.nect
                    currentNode.next = None
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1


    def deleteEnd(self):
        # head => John -> Ben -> Mattew -> None
        if self.isListEmpty() is False:
            if self.head.next is None:
                self.deleteHead()
                return
            lastNode = self.head
            while lastNode.next is not None:
                previousNode = lastNode
                lastNode = lastNode.next
            previousNode.next = None
        else:
            print("Linked List is empty. Delete failed")

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

# # Node => data, next
# # firstNode.data => John, firstNode.next => None
# firstNode = Node("John")
# linkedList = LinkedList()
# linkedList.insertEnd(firstNode)
# secondNode = Node("Ben")
# linkedList = LinkedList()
# linkedList.insertEnd(secondNode)
# thirdNode = Node("Matthew")
# linkedList.insertHead(thirdNode)
# linkedList.printList()



