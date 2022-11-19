# Print the middle node of a Singly Linked List

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

    ___ listLength
        length _ 0
        currentNode _ head
        _____ currentNode __ n.. N..
            length +_ 1
            currentNode _ currentNode.n..
        r_ length

    ___ printMiddle
        length _ listLength()
        __ length !_ 0:
            __ length __ 1:
                print("Middle Node: ",head.data)
                r_
            middlePosition _ length // 2
            middleNode _ head
            _____ middlePosition !_ 0:
                middleNode _ middleNode.n..
                middlePosition -_ 1
            print("Middle Node: ",middleNode.data)

nodeOne _ Node(1)
nodeTwo _ Node(5)
nodeThree _ Node(3)
nodeFour _ Node(10)
nodeFive _ Node(6)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
linkedList.printMiddle()
