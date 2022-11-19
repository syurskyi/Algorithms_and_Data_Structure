c_ Node:
    ___ -  data
        ? _ ?
        n.. _ N..
        previous _ N..

c_ LinkedList
    ___ -  
        head _ N..

    ___ listLength 
        # 10->20->None
        length _ 0
        currentNode _ head
        _____ currentNode __ n.. N..
            currentNode _ currentNode.n..
            length +_ 1
        r_ length

    ___ insertHead newNode
        previousHead _ head
        head _ newNode
        head.n.. _ previousHead
        previousHead.previous _ head

    ___ insertAt newNode, position
        # 10->30->20 || position +> 1
        __ position < 0 __ position > listLength(
            print("Invalid position")
            r_
        __ position __ listLength(
            insertEnd(newNode)
            r_
        __ position __ 0:
            insertHead(newNode)
            r_
        currentNode _ head
        currentPosition _ 0
        _____ T..:
            __ currentPosition __ position:
                currentNode.previous.n.. _ newNode
                ?.previous _ currentNode.previous
                ?.n.. _ currentNode
                currentNode.previous _ newNode
                b..
            currentNode _ currentNode.n..
            currentPosition +_ 1

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

    ___ deleteHead 
        head _ head.n..
        head.previous.n.. _ N..
        head.previous _ N..

    ___ deleteAt position
        currentNode _ head
        currentPosition _ 0
        _____ T..:
            __ currentPosition __ position:
                currentNode.previous.n.. _ currentNode.n..
                currentNode.n...previous _ currentNode.previous
                currentNode.n.. _ N..
                currentNode.previous _ N..
                b..
            currentNode _ currentNode.n..
            currentPosition +_ 1

    ___ deleteEnd 
        currentNode _ head
        _____ T..:
            __ currentNode.n...next __ N..
                currentNode.n...previous _ N..
                currentNode.n...n.. _ N..
                currentNode.n.. _ N..
                b..
            currentNode _ currentNode.n..

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

# nodeOne = Node('Joe')
# nodeTwo = Node('Mary')
# nodeThree = Node('Grace')
# linkedList = LinkedList()
# linkedList.insertEnd(nodeOne)
# linkedList.insertEnd(nodeTwo)
# linkedList.insertHead(nodeThree)
# linkedList.deleteAt(0)
# linkedList.printList()

