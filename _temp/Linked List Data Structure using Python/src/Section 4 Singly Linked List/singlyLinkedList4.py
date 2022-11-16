# Create nodes
# Create linked list
# Add nodes to linked list
# Print linked list

c_ Node:
    ___ -  data
        data _ data
        next _ N..

c_ LinkedList:
    ___ -
        head _ N..

    ___ isListEmpty
        __ head __ N..:
            r_ T..
        ____
            r_ F..

    ___ insertHead newNode
        # data = > Matthew, next => None
        temporaryNode _ head # John
        head _ newNode # Matthew
        head.next _ temporaryNode
        d.. temporaryNode

    ___ listLength
        currentNode _ head
        length _ 0
        _____ currentNode __ n.. N..:
            length +_ 1
            currentNode _ currentNode.next
        r_ length

    ___ insertAt newNode, position
        # head =>10->20->None || newNode => 15 -> None || position=>1
        __ position < 0 __ position > listLength(
            print("Invalid position")
            r_
        __ position __ 0:
            insertHead(newNode)
            r_
        currentNode _ head # 10, 20
        currentPosition _ 0 # 0, 1
        _____ T..:
            __ currentPosition __ position:
                previousNode.next _ newNode
                newNode.next _ currentNode
                b..
            previousNode _ currentNode
            currentNode _ currentNode.next
            currentPosition +_ 1


    ___ insertEnd newNode
        __ head __ N..:
            head _ newNode
        ____
            lastNode _ head
            _____ T..:
                __ lastNode.next __ N..:
                    b..
                lastNode _ lastNode.next
            lastNode.next _ newNode

    ___ deleteHead
        __ isListEmpty() __ F..:
            # head => 10 -> 15 -> 20 || 15->20->10-> None
            previousHead _ head
            head _ head.next
            previousHead.next _ N..
        ____
            print("Linked List is empty. Delete failed")

    ___ deleteEnd
        # head => John -> Ben -> Mattew -> None
        __ isListEmpty() __ F..:
            __ head.next __ N..:
                deleteHead()
                r_
            lastNode _ head
            _____ lastNode.next __ n.. N..:
                previousNode _ lastNode
                lastNode _ lastNode.next
            previousNode.next _ N..
        ____
            print("Linked List is empty. Delete failed")

    ___ printList
        # head => John -> Ben -> Matthew -> None
        __ head __ N..:
            print("List is empty")
            r_
        currentNode _ head
        _____ T..:
            __ currentNode __ N..:
                b..
            print(currentNode.data)
            currentNode _ currentNode.next


# Node => data, next
# firstNode.data => John, firstNode.next => None
firstNode _ Node(10)
linkedList _ LinkedList()
linkedList.insertEnd(firstNode)
secondNode _ Node(15)
linkedList _ LinkedList()
linkedList.insertEnd(secondNode)
thirdNode _ Node(20)
linkedList.deleteEnd()
linkedList.printList()


