# In an integer linked list, count the number of nodes that are even and the number of nodes that are odd

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

    ___ countNodes
        currentNode _ head
        evenCount _ 0
        oddCount _ 0
        _____ currentNode __ n.. N..:
            __ currentNode.data % 2 __ 0:
                evenCount +_ 1
            ____
                oddCount +_ 1
            currentNode _ currentNode.next
        print("Even Nodes: ",evenCount)
        print("Odd Nodes: ", oddCount)

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
linkedList.countNodes()
