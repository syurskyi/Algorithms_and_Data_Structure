from doublyLinkedList import Node, LinkedList

___ removeDuplicate(linkedList
    # 13->5->13->2->13->None
    nodeCount _ {}
    # {13: 1, 5:1, 2:1}
    currentNode _ linkedList.head
    _____ T..:
        __ currentNode.data n.. __ nodeCount.keys(
            nodeCount[currentNode.data] _ 1
        ____
            nodeCount[currentNode.data] +_ 1
        __ currentNode.next __ N..:
            _____ T..:
                __ currentNode.previous __ N..:
                    break
                previousNode _ currentNode.previous
                __ nodeCount[currentNode.data] > 1:
                    currentNode.previous.next _ currentNode.next
                    __ currentNode.next __ n.. N..:
                        currentNode.next.previous _ currentNode.previous
                    currentNode.next _ N..
                    currentNode.previous _ N..
                    nodeCount[currentNode.data] -_ 1
                currentNode _ previousNode
            break    
        currentNode _ currentNode.next


nodeOne _ Node(13)
nodeTwo _ Node(5)
nodeThree _ Node(13)
nodeFour _ Node(2)
nodeFive _ Node(13)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
removeDuplicate(linkedList)
linkedList.printList()
