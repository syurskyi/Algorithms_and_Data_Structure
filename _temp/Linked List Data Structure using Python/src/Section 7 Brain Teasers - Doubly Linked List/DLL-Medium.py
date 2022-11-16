# Swap the first node and last node of a doubly linked list

c_ Node:
    ___ -  data
        data _ data
        next _ N..
        previous _ N..

c_ LinkedList:
    ___ -
        head _ N..

    ___ insertEnd newNode
        __ head __ N..:
            head _ newNode
            r_
        currentNode _ head
        _____ currentNode.next __ n.. N..:
            currentNode _ currentNode.next
        currentNode.next _ newNode
        newNode.previous _ currentNode

    ___ swapHead
        __ head __ N..:
            print("Empty list")
            r_
        # List has just 1 Node
        __ head.next __ N..:
            r_
        lastNode _ head
        _____ lastNode.next __ n.. N..:
            lastNode _ lastNode.next
        currentHead _ head
        # Change previous pointer of head
        head.previous _ lastNode.previous
        # Change previous pointer of next node of head
        head.next.previous _ lastNode
        # Change next pointer of last node
        lastNode.next _ head.next
        # Change next pointer of previous node of last node
        lastNode.previous.next _ head
        # Change next pointer of head
        head.next _ N..
        # Change previous pointer of last node
        lastNode.previous _ N..
        # Make last node as head node
        head _ lastNode


    ___ printList
        __ head __ N..:
            print("Empty list")
            r_
        currentNode _ head
        print("Printing from beginning")
        _____ T..:
            print(currentNode.data)
            __ currentNode.next __ N..:
                b..
            currentNode _ currentNode.next
        print("Printing from end")
        _____ T..:
            print(currentNode.data)
            __ currentNode.previous __ N..:
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
