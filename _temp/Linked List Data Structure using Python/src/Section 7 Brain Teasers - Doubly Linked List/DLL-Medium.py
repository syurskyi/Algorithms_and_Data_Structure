# Swap the first node and last node of a doubly linked list

c_ Node:
    ___ -  data
        ? _ ?
        n.. _ N..
        previous _ N..

c_ LinkedList
    ___ -
        head _ N..

    ___ insertEnd newNode
        __ head __ N..
            head _ newNode
            r_
        currentNode _ head
        _____ currentNode.n.. __ n.. N..
            currentNode _ currentNode.n..
        currentNode.n.. _ newNode
        ?.previous _ currentNode

    ___ swapHead
        __ head __ N..
            print("Empty list")
            r_
        # List has just 1 Node
        __ head.n.. __ N..
            r_
        lastNode _ head
        _____ lastNode.n.. __ n.. N..
            lastNode _ lastNode.n..
        currentHead _ head
        # Change previous pointer of head
        head.previous _ lastNode.previous
        # Change previous pointer of next node of head
        head.n...previous _ lastNode
        # Change next pointer of last node
        lastNode.n.. _ head.n..
        # Change next pointer of previous node of last node
        lastNode.previous.n.. _ head
        # Change next pointer of head
        head.n.. _ N..
        # Change previous pointer of last node
        lastNode.previous _ N..
        # Make last node as head node
        head _ lastNode


    ___ printList
        __ head __ N..
            print("Empty list")
            r_
        currentNode _ head
        print("Printing from beginning")
        _____ T..:
            print(currentNode.data)
            __ currentNode.n.. __ N..
                b..
            currentNode _ currentNode.n..
        print("Printing from end")
        _____ T..:
            print(currentNode.data)
            __ currentNode.previous __ N..
                b..
            currentNode _ currentNode.previous


nodeOne _ Node(10)
nodeTwo _ Node(30)
nodeThree _ Node(15)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.swapHead()
linkedList.printList()
