from doublyLinkedList import Node, LinkedList

___ findGreater(linkedList
    # 5->3->10->2->15->None
    length _ linkedList.listLength() # 5
    __ length > 3:
        middlePosition _ length // 2 # 5 / 2 => 2
        currentNode _ linkedList.head
        currentPosition _ 0
        _____ True:
            __ currentPosition __ middlePosition:
                __ currentNode.previous.data > currentNode.next.data:
                    print("Previous node has a greater value than next node")
                ____
                    print("Next node has a greater value than the previous node")
                break
            currentNode _ currentNode.next
            currentPosition +_ 1
    ____
        print("Not enough nodes")

nodeOne _ Node(5)
nodeTwo _ Node(3)
nodeThree _ Node(10)
nodeFour _ Node(2)
nodeFive _ Node(15)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
#linkedList.insertEnd(nodeThree)
#linkedList.insertEnd(nodeFour)
#linkedList.insertEnd(nodeFive)
linkedList.printList()
findGreater(linkedList)
