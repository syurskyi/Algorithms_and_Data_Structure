# Delete a node with the given data in a doubly linked list

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

    ___ deleteNode data
        currentNode _ head
        _____ currentNode __ n.. N..
            __ currentNode.data __ data:
                # head node deletion
                __ currentNode __ head:
                    head _ currentNode.n..
                    currentNode.n.. _ N..
                    __ head __ n.. N..
                        head.previous _ N..
                    r_
                # last node deletion
                __ currentNode.n.. __ N..
                    currentNode.previous.n.. _ N..
                    currentNode.previous _ N..
                    r_
                # node in between two nodes
                currentNode.n...previous _ currentNode.previous
                currentNode.previous.n.. _ currentNode.n..
                currentNode.n.. _ N..
                currentNode.previous _ N..
                r_
            currentNode _ currentNode.n..
        print("Data not found")

    ___ printList
        __ head __ N..
            print("Empty list")
            r_
        currentNode _ head
        _____ currentNode __ n.. N..
            print(currentNode.data)
            currentNode _ currentNode.n..

nodeOne _ Node(10)
nodeTwo _ Node(30)
nodeThree _ Node(15)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.deleteNode(30)
linkedList.printList()
