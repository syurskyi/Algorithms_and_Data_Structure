c_ Node:
    ___ -  data
        ? _ ?
        n.. _ N..
        previous _ N..

c_ LinkedList
    ___ -
        head _ N..

    ___ insertHead newNode
        previousHead _ head
        head _ newNode
        head.n.. _ previousHead
        previousHead.previous _ head

    ___ insertEnd newNode
        # (head=> Joe->Mary->Grace->None || head=>None <-Joe<-Mary<-Grace
        __ head __ N..
            head _ newNode
            r_
        currentNode _ head
        _____ T..:
            __ currentNode.n.. __ N..
                b..
            currentNode _ currentNode.n..
        currentNode.n.. _ newNode
        ?.previous _ currentNode

    ___ printList
        __ head __ N..
            print("List is empty")
            r_
        currentNode _ head
        print("Printing from the beginning")
        _____ T..:
            __ currentNode __ N..
                b..
            print(currentNode.data)
            __ currentNode.n.. __ N..
                reverseTraversalNode _ currentNode
            currentNode _ currentNode.n..
        print("Printing form end")
        _____ T..:
            __ reverseTraversalNode __ N..
                b..
            print(reverseTraversalNode.data)
            reverseTraversalNode _ reverseTraversalNode.previous

nodeOne _ Node('Joe')
nodeTwo _ Node('Mary')
nodeThree _ Node('Grace')
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertHead(nodeThree)
linkedList.printList()

