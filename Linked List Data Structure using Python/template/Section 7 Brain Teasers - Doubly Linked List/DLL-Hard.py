# Merge two unsorted list into a sorted list such that final list has no duplicate values

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

    def printList(self):
        if self.head is None:
            print("Empty list")
            return
        currentNode = self.head
        while True:
            print(currentNode.data)
            if currentNode.next is None:
                break
            currentNode = currentNode.next

def isDuplicate(currentNode, mergedList):
    currentMerge = mergedList.head
    # Check if data already exists in list
    while currentMerge is not None:
        if currentNode.data == currentMerge.data:
            return True
        currentMerge = currentMerge.next
    return False

def sortNodeOrder(currentNode, mergedList):
    currentMerge = mergedList.head
    while True:
        # Insert in sorted order
        if currentNode.data < currentMerge.data:
            # Check if currentNode is to be made the new head node
            if currentMerge is mergedList.head:
                currentNode.next = currentMerge
                currentMerge.previous = currentNode
                mergedList.head = currentNode
            else:
                currentNode.previous = currentMerge.previous
                currentNode.next = currentMerge
                currentMerge.previous.next = currentNode
                currentMerge.previous = currentNode
            return
        else:
            if currentMerge.next is None:
                currentMerge.next = currentNode
                currentNode.previous = currentMerge
                return
            currentMerge = currentMerge.next

def mergeList(linkedListOne, linkedListTwo, mergedList):
    currentFirst = linkedListOne.head
    currentSecond = linkedListTwo.head
    # Insert list one into merged list
    while True:
        if currentFirst is None:
            break
        currentFirstNext = currentFirst.next
        currentFirst.next = None
        currentFirst.previous = None
        if mergedList.head is None:
            mergedList.head = currentFirst
            currentFirst = currentFirstNext
            continue
        # Check if node already exists
        if isDuplicate(currentFirst, mergedList) is False:
            # Place the node in sorted order
            sortNodeOrder(currentFirst, mergedList)
        currentFirst = currentFirstNext
    # Insert list two into merged list
    while True:
        if currentSecond is None:
            break
        currentSecondNext = currentSecond.next
        currentSecond.next = None
        currentSecond.previous = None
        if mergedList.head is None:
            mergedList.head = currentSecond
            currentSecond = currentSecondNext
            continue
        # Check if node already exists
        if isDuplicate(currentSecond, mergedList) is False:
            # Place the node in sorted order
            sortNodeOrder(currentSecond, mergedList)
        currentSecond = currentSecondNext



linkedListOne = LinkedList()
nodeOne = Node(5)
nodeTwo = Node(10)
nodeThree = Node(7)
nodeFour = Node(5)
linkedListOne.insertEnd(nodeOne)
linkedListOne.insertEnd(nodeTwo)
linkedListOne.insertEnd(nodeThree)
linkedListOne.insertEnd(nodeFour)

linkedListTwo = LinkedList()
nodeFive = Node(23)
nodeSix = Node(7)
nodeSeven = Node(1)
nodeEight = Node(7)
linkedListTwo.insertEnd(nodeFive)
linkedListTwo.insertEnd(nodeSix)
linkedListTwo.insertEnd(nodeSeven)
linkedListTwo.insertEnd(nodeEight)


print("Printing List 1")
linkedListOne.printList()
print("Printing List 2")
linkedListTwo.printList()
print("Done")
mergedList = LinkedList()
mergeList(linkedListOne, linkedListTwo, mergedList)

print("Printing Merged List")
mergedList.printList()
