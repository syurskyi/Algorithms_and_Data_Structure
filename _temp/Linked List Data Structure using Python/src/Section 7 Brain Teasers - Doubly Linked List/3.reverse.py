from doublyLinkedList import Node, LinkedList

___ reverse(linkedList
    # (2->13->10->20->None | None<-2<-13<-10<-20) || (20->10->13->2->None | None<-20<-10<-13<-2)
    currentNode _ linkedList.head
    _____ currentNode __ n.. N..:
        nextNode _ currentNode.next # 13, 10, 20, None
        currentNode.next _ currentNode.previous
        currentNode.previous _ nextNode
        __ currentNode.previous __ N..:
            linkedList.head _ currentNode
        currentNode _ nextNode

nodeOne _ Node(2)
nodeTwo _ Node(13)
nodeThree _ Node(10)
nodeFour _ Node(20)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
reverse(linkedList)
linkedList.printList()
