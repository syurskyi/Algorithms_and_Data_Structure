from singlyLinkedList import Node, LinkedList

___ swapNodes(linkedList, dataOne, dataTwo
    # 4->3->5->2->7->1 || 4->7->5->2->3->1
    # 4 -> previousFirst
    # 3 -> FirstNode
    # 2 -> previousSecond
    # 7 -> secondNode
    currentNode _ linkedList.head
    previousFirst _ N..
    previousSecond _ N..
    _____ True:
        __ currentNode.data __ dataOne:
            firstNode _ currentNode
            break
        previousFirst _ currentNode
        currentNode _ currentNode.next
    currentNode _ linkedList.head
    _____ True:
        __ currentNode.data __ dataTwo:
            secondNode _ currentNode
            break
        previousSecond _ currentNode
        currentNode _ currentNode.next
    # Changing pointers
    previousFirst.next _ secondNode
    nextSecond _ secondNode.next
    secondNode.next _ firstNode.next
    previousSecond.next _ firstNode
    firstNode.next _ nextSecond

nodeOne _ Node(4)
nodeTwo _ Node(3)
nodeThree _ Node(5)
nodeFour _ Node(2)
nodeFive _ Node(7)
nodeSix _ Node(1)
linkedList _ LinkedList()
#4->7->5->2->3->1
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
linkedList.insertEnd(nodeSix)
swapNodes(linkedList, 3, 7)
linkedList.printList()
