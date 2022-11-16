c_ Node:
    ___ -  data
        data _ data
        next _ N..
        previous _ N..

c_ LinkedList:
    ___ -  
        head _ N..

    ___ insertHead newNode
        __ head __ N..:
            head _ newNode
            head.previous _ head
            r_
        lastNode _ head.previous
        newNode.previous _ lastNode
        newNode.next _ head
        head.previous _ newNode
        head _ newNode
        lastNode.next _ head

    ___ insertEnd newNode
        __ head __ N..:
            head _ newNode
            head.next _ head
            head.previous _ head
            r_
        currentNode _ head
        _____ currentNode.next __ n.. head:
            currentNode _ currentNode.next
        currentNode.next _ newNode
        newNode.previous _ currentNode
        newNode.next _ head
        head.previous_newNode

    ___ deleteHead 
        __ head __ N..:
            print("Empty list")
            r_
        previousHead _ head
        head _ head.next
        head.previous _ previousHead.previous
        previousHead.previous.next _ head
        previousHead.previous _ N..
        previousHead.next _ N..

    ___ deleteEnd 
        __ head __ N..:
            print("Empty List")
            r_
        currentNode _ head
        _____ T..:
            __ currentNode.next.next __ head:
                b..
            currentNode _ currentNode.next
        head.previous _ currentNode
        currentNode.next.previous _ N..
        currentNode.next.next _ N..
        currentNode.next _ head

    ___ printList 
        __ head __ n.. N..:
            currentNode _ head
            _____ T..:
                print(currentNode.data)
                currentNode _ currentNode.next
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
