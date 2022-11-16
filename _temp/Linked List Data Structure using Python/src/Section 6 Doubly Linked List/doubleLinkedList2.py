c_ Node:
    ___ -  data
        data _ data
        next _ N..
        previous _ N..

c_ LinkedList:
    ___ -
        head _ N..

    ___ insertHead newNode
        previousHead _ head
        head _ newNode
        head.next _ previousHead
        previousHead.previous _ head

    ___ insertEnd newNode
        # (head=> Joe->Mary->Grace->None || head=>None <-Joe<-Mary<-Grace
        __ head __ N..:
            head _ newNode
            r_
        currentNode _ head
        _____ T..:
            __ currentNode.next __ N..:
                break
            currentNode _ currentNode.next
        currentNode.next _ newNode
        newNode.previous _ currentNode

    ___ printList
        __ head __ N..:
            print("List is empty")
            r_
        currentNode _ head
        print("Printing from the beginning")
        _____ T..:
            __ currentNode __ N..:
                break
            print(currentNode.data)
            __ currentNode.next __ N..:
                reverseTraversalNode _ currentNode
            currentNode _ currentNode.next
        print("Printing form end")
        _____ T..:
            __ reverseTraversalNode __ N..:
                break
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

