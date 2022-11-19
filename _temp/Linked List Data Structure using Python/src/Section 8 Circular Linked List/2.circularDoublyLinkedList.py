c_ Node:
    ___ -  data
        ? _ ?
        n.. _ N..
        previous _ N..

c_ LinkedList
    ___ -  
        head _ N..

    ___ insertHead newNode
        __ head __ N..
            head _ newNode
            head.previous _ head
            r_
        lastNode _ head.previous
        ?.previous _ lastNode
        ?.n.. _ head
        head.previous _ newNode
        head _ newNode
        lastNode.n.. _ head

    ___ insertEnd newNode
        __ head __ N..
            head _ newNode
            head.n.. _ head
            head.previous _ head
            r_
        currentNode _ head
        _____ currentNode.n.. __ n.. head:
            currentNode _ currentNode.n..
        currentNode.n.. _ newNode
        ?.previous _ currentNode
        ?.n.. _ head
        head.previous_newNode

    ___ deleteHead 
        __ head __ N..
            print("Empty list")
            r_
        previousHead _ head
        head _ head.n..
        head.previous _ previousHead.previous
        previousHead.previous.n.. _ head
        previousHead.previous _ N..
        previousHead.n.. _ N..

    ___ deleteEnd 
        __ head __ N..
            print("Empty List")
            r_
        currentNode _ head
        _____ T..:
            __ currentNode.n...next __ head:
                b..
            currentNode _ currentNode.n..
        head.previous _ currentNode
        currentNode.n...previous _ N..
        currentNode.n...n.. _ N..
        currentNode.n.. _ head

    ___ printList 
        __ head __ n.. N..
            currentNode _ head
            _____ T..:
                print(currentNode.data)
                currentNode _ currentNode.n..
                __ currentNode __ head:
                    b..
            # Print previous of head node to verify the connection to last node
            print(currentNode.previous.data)

nodeOne _ Node(10)
nodeTwo _ Node(20)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertHead(nodeTwo)
linkedList.deleteEnd()
linkedList.printList()
