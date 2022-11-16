# Delete nodes that have a greater value on the right side

c_ Node:
    ___ -  data
        data _ data
        next _ N..

c_ LinkedList:
    ___ -  
        head _ N..

    ___ insertEnd newNode
        __ head __ N..:
            head _ newNode
            r_
        lastNode _ head
        _____ lastNode.next __ n.. N..:
            lastNode _ lastNode.next
        lastNode.next _ newNode

    ___ deleteRight 
        currentNode _ head
        _____ currentNode.next __ n.. N..:
            # Check if node on the right has a greater value
            __ currentNode.next.data > currentNode.data:
                # If currentNode is the head node, delete it and make the new node as the head node
                __ currentNode __ head:
                    head _ currentNode.next
                    currentNode.next _ N..
                    currentNode _ head
                    continue
                # If currentNode is not head node, make the previous node point to next node and remove this node
                previousNode.next _ currentNode.next
                currentNode.next _ N..
                currentNode _ head
            ____
                # Advance to next node if the data on the right side is not greater than currentNode
                previousNode _ currentNode
                currentNode _ currentNode.next

    ___ printList 
        __ head __ N..:
            print("Empty List")
            r_
        currentNode _ head
        _____ currentNode __ n.. N..:
            print(currentNode.data)
            currentNode _ currentNode.next

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
