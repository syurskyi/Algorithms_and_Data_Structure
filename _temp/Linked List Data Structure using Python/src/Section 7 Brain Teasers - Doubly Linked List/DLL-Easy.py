# Delete a node with the given data in a doubly linked list

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

    ___ deleteNode data
        currentNode _ head
        _____ currentNode __ n.. N..:
            __ currentNode.data == data:
                # head node deletion
                __ currentNode __ head:
                    head _ currentNode.next
                    currentNode.next _ N..
                    __ head __ n.. N..:
                        head.previous _ N..
                    r_
                # last node deletion
                __ currentNode.next __ N..:
                    currentNode.previous.next _ N..
                    currentNode.previous _ N..
                    r_
                # node in between two nodes
                currentNode.next.previous _ currentNode.previous
                currentNode.previous.next _ currentNode.next
                currentNode.next _ N..
                currentNode.previous _ N..
                r_
            currentNode _ currentNode.next
        print("Data not found")

    ___ printList
        __ head __ N..:
            print("Empty list")
            r_
        currentNode _ head
        _____ currentNode __ n.. N..:
            print(currentNode.data)
            currentNode _ currentNode.next

nodeOne _ Node(10)
nodeTwo _ Node(30)
nodeThree _ Node(15)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.deleteNode(30)
linkedList.printList()
