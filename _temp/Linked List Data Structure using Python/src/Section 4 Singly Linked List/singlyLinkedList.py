# Create nodes
# Create linked list
# Add nodes to linked list
# Print linked list

c_ Node:
    ___ -  data
        ? _ ?
        n.. _ N..

c_ LinkedList
    ___ -  
        head _ N..

    ___ i..  newNode
        # head=>John->None
        __ head __ N..
            head _ newNode
        ____
            # head=>John->Ben->None || John -> Matthew
            lastNode _ head
            _____ T..:
                __ lastNode.n.. __ N..
                    b..
                lastNode _ lastNode.n..
            lastNode.n.. _ newNode

    ___ printList 
        # head => John -> Ben -> Matthew -> None
        __ head __ N..
            print("List is empty")
            r_
        currentNode _ head
        _____ T..:
            __ currentNode __ N..
                b..
            print(currentNode.data)
            currentNode _ currentNode.n..


# Node => data, next
# firstNode.data => John, firstNode.next => None
firstNode _ Node("John")
linkedList _ LinkedList()
linkedList.i.. (firstNode)
secondNode _ Node("Ben")
linkedList _ LinkedList()
linkedList.i.. (secondNode)
thirdNode _ Node("Matthew")
linkedList.i.. (thirdNode)
linkedList.printList()

