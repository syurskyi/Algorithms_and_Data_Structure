c_ Node:
    ___ -  data
        data _ data
        next _ N..
        previous _ N..

c_ LinkedList:
    ___ -
        head _ N..

    ___ listLength
        # 10->20->None
        length _ 0
        currentNode _ head
        _____ currentNode __ n.. N..:
            currentNode _ currentNode.next
            length +_ 1
        r_ length

    ___ insertHead newNode
        previousHead _ head
        head _ newNode
        head.next _ previousHead
        previousHead.previous _ head

    ___ insertAt newNode, position
        # 10->30->20 || position +> 1
        __ position < 0 or position > listLength(
            print("Invalid position")
        __ position __ listLength(
            insertEnd(newNode)
            r_
        __ position __ 0:
            insertHead(newNode)
            r_
        currentNode _ head
        currentPosition _ 0
        _____ True:
            __ currentPosition == position:
                currentNode.previous.next _ newNode
                newNode.previous _ currentNode.previous
                newNode.next _ currentNode
                currentNode.previous _ newNode
                break
            currentNode _ currentNode.next
            currentPosition +_ 1

    ___ insertEnd newNode
        # (head=> Joe->Mary->Grace->None || head=>None <-Joe<-Mary<-Grace
        __ head __ N..:
            head _ newNode
            r_
        currentNode _ head
        _____ True:
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
        _____ True:
            __ currentNode __ N..:
                break
            print(currentNode.data)
            __ currentNode.next __ N..:
                reverseTraversalNode _ currentNode
            currentNode _ currentNode.next
        print("Printing form end")
        _____ True:
            __ reverseTraversalNode __ N..:
                break
            print(reverseTraversalNode.data)
            reverseTraversalNode _ reverseTraversalNode.previous

nodeOne _ Node(10)
nodeTwo _ Node(20)
nodeThree _ Node(30)
linkedList _ LinkedList()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertAt(nodeThree, 2)
linkedList.printList()

