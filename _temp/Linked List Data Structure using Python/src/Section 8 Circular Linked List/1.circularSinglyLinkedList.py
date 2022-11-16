c_ Node:
    ___ -  data
        data _ data
        next _ N..

c_ LinkedList:
    ___ -  
        head _ N..

    ___ insertEnd newNode
        __ head __ N..:
            head _ newNode
            newNode.next _ head
            r_
        currentNode _ head
        _____(currentNode.next __ n.. head
            currentNode _ currentNode.next
        currentNode.next _ newNode
        newNode.next _ head

    ___ insertHead newNode
        lastNode _ head
        _____(lastNode.next __ n.. head
            lastNode _ lastNode.next
        previousHead _ head
        head _ newNode
        newNode.next _ previousHead
        lastNode.next _ head

    ___ deleteEnd 
        lastNode _ head
        _____(lastNode.next __ n.. head
            previousNode _ lastNode
            lastNode _ lastNode.next
        lastNode.next _ N..
        previousNode.next _ head

    ___ deleteHead 
        lastNode _ head
        _____(lastNode.next __ n.. head
            lastNode _ lastNode.next
        previousHead _ head
        head _ head.next
        lastNode.next _ head
        previousHead.next _ N..

    ___ printList 
        currentNode _ head
        _____ T..:
            print(currentNode.data)
            currentNode _ currentNode.next
            __ currentNode __ head:
                break
        print(currentNode.data)

nodeOne _ Node(10)
nodeTwo _ Node(20)
nodeThree _ Node(30)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.deleteHead()
linkedList.printList()
