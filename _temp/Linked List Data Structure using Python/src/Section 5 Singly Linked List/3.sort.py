from singlyLinkedList import Node, LinkedList

___ swapNext(linkedList, previousNode, largestNode, nextNode
    # 4->3->5->1 || 3->4->5->1 || 4->|1->5->None
    largestNode.n.. _?.n..
    nextNode.n.. _ largestNode
    __ largestNode __ linkedList.head:
        linkedList.head _ nextNode
        r_
    previousNode.n.. _  nextNode

___ sort(linkedList
    # number of iterations = number of nodes - 1
    numberOfIterations _ linkedList.listLength() - 1 # 3
    _____ numberOfIterations !_ 0: # 3, 2, 1
        largestNode _ linkedList.head
        previousNode _ N..
        numberOfComparisons _ numberOfIterations
        _____ numberOfComparisons !_ 0:
            __ largestNode.data > largestNode.n...data:
                swapNext(linkedList, previousNode, largestNode, largestNode.n..)
            ____
                previousNode _ largestNode
                largestNode _ largestNode.n..
            numberOfComparisons -_ 1

        numberOfIterations -_ 1

nodeOne _ Node(4)
nodeTwo _ Node(3)
nodeThree _ Node(5)
nodeFour _ Node(1)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
sort(linkedList)
linkedList.printList()
