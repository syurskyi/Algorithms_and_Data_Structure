# Delete nodes that have a greater value on the right side

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
            r_
        lastNode _ head
        _____ lastNode.n.. __ n.. N..
            lastNode _ lastNode.n..
        lastNode.n.. _ newNode

    ___ deleteRight 
        currentNode _ head
        _____ currentNode.n.. __ n.. N..
            # Check if node on the right has a greater value
            __ currentNode.n...data > currentNode.data:
                # If currentNode is the head node, delete it and make the new node as the head node
                __ currentNode __ head:
                    head _ currentNode.n..
                    currentNode.n.. _ N..
                    currentNode _ head
                    c..
                # If currentNode is not head node, make the previous node point to next node and remove this node
                previousNode.n.. _ currentNode.n..
                currentNode.n.. _ N..
                currentNode _ head
            ____
                # Advance to next node if the data on the right side is not greater than currentNode
                previousNode _ currentNode
                currentNode _ currentNode.n..

    ___ printList 
        __ head __ N..
            print("Empty List")
            r_
        currentNode _ head
        _____ currentNode __ n.. N..
            print(currentNode.data)
            currentNode _ currentNode.n..

nodeOne _ Node(10)
nodeTwo _ Node(5)
nodeThree _ Node(6)
nodeFour _ Node(2)
nodeFive _ Node(3)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
linkedList.deleteRight()
linkedList.printList()
