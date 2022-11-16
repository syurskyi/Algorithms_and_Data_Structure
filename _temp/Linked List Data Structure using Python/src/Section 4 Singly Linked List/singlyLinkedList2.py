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

    ___ insertHead newNode
        # data = > Matthew, next => None
        temporaryNode _ head # John
        head _ newNode # Matthew
        head.next _ temporaryNode
        d.. temporaryNode

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
firstNode _ Node("John")
linkedList _ LinkedList()
linkedList.insertEnd(firstNode)
secondNode _ Node("Ben")
linkedList _ LinkedList()
linkedList.insertEnd(secondNode)
thirdNode _ Node("Matthew")
linkedList.insertHead(thirdNode)
linkedList.printList()

