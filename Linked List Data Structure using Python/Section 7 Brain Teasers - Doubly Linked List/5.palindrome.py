from doublyLinkedList import Node, LinkedList

def palindrome(linkedList):
    # L, E, V, E, L
    startPointer = linkedList.head
    endPointer = linkedList.head
    while endPointer.next is not None:
        endPointer = endPointer.next
    while True:
        if startPointer == endPointer:
            print("List is palindrome")
            return
        if startPointer.data == endPointer.data:
            startPointer = startPointer.next
            endPointer = endPointer.previous
        else:
            print("List is not palindrome")
            return

nodeOne = Node('I')
nodeTwo = Node('N')
nodeThree = Node('D')
nodeFour = Node('E')
nodeFive = Node('X')
linkedList = LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
linkedList.printList()
palindrome(linkedList)
