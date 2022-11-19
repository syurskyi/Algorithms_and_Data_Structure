c_ Node:
    ___ -  data
        ? _ ?
        n.. _ N..

c_ LinkedList
    ___ -  
        head _ N..

    ___ insertEnd newNode
        __ head __ N..
            head _ newNode
            ?.n.. _ head
            r_
        currentNode _ head
        _____(currentNode.n.. __ n.. head
            currentNode _ currentNode.n..
        currentNode.n.. _ newNode
        ?.n.. _ head

    ___ insertHead newNode
        lastNode _ head
        _____(lastNode.n.. __ n.. head
            lastNode _ lastNode.n..
        previousHead _ head
        head _ newNode
        ?.n.. _ previousHead
        lastNode.n.. _ head

    ___ deleteEnd 
        lastNode _ head
        _____(lastNode.n.. __ n.. head
            previousNode _ lastNode
            lastNode _ lastNode.n..
        lastNode.n.. _ N..
        previousNode.n.. _ head

    ___ deleteHead 
        lastNode _ head
        _____(lastNode.n.. __ n.. head
            lastNode _ lastNode.n..
        previousHead _ head
        head _ head.n..
        lastNode.n.. _ head
        previousHead.n.. _ N..

    ___ printList 
        currentNode _ head
        _____ T..:
            print(currentNode.data)
            currentNode _ currentNode.n..
            __ currentNode __ head:
                b..
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
