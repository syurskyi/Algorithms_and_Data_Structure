from singlyLinkedList import Node, LinkedList

___ removeDuplicate(linkedList
    # 1->2->3->3->5
    currentNode _ linkedList.head
    _____ True:
        __ currentNode.data == currentNode.next.data:
            duplicateNode _ currentNode.next
            currentNode.next _ duplicateNode.next
            duplicateNode.next _ N..
            break
        currentNode _ currentNode.next


nodeOne _ Node(1)
nodeTwo _ Node(2)
nodeThree _ Node(3)
nodeFour _ Node(3)
nodeFive _ Node(5)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
removeDuplicate(linkedList)
linkedList.printList()
