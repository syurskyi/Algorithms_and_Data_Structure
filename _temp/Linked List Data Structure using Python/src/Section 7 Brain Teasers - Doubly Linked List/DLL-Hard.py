# Merge two unsorted list into a sorted list such that final list has no duplicate values

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

    ___ printList 
        __ head __ N..
            print("Empty list")
            r_
        currentNode _ head
        _____ T..:
            print(currentNode.data)
            __ currentNode.n.. __ N..
                b..
            currentNode _ currentNode.n..

___ isDuplicate(currentNode, mergedList
    currentMerge _ mergedList.head
    # Check if data already exists in list
    _____ currentMerge __ n.. N..
        __ currentNode.data __ currentMerge.data:
            r_ T..
        currentMerge _ currentMerge.n..
    r_ F..

___ sortNodeOrder(currentNode, mergedList
    currentMerge _ mergedList.head
    _____ T..:
        # Insert in sorted order
        __ currentNode.data < currentMerge.data:
            # Check if currentNode is to be made the new head node
            __ currentMerge __ mergedList.head:
                currentNode.n.. _ currentMerge
                currentMerge.previous _ currentNode
                mergedList.head _ currentNode
            ____
                currentNode.previous _ currentMerge.previous
                currentNode.n.. _ currentMerge
                currentMerge.previous.n.. _ currentNode
                currentMerge.previous _ currentNode
            r_
        ____
            __ currentMerge.n.. __ N..
                currentMerge.n.. _ currentNode
                currentNode.previous _ currentMerge
                r_
            currentMerge _ currentMerge.n..

___ mergeList(linkedListOne, linkedListTwo, mergedList
    currentFirst _ linkedListOne.head
    currentSecond _ linkedListTwo.head
    # Insert list one into merged list
    _____ T..:
        __ currentFirst __ N..
            b..
        currentFirstNext _ currentFirst.n..
        currentFirst.n.. _ N..
        currentFirst.previous _ N..
        __ mergedList.head __ N..
            mergedList.head _ currentFirst
            currentFirst _ currentFirstNext
            c..
        # Check if node already exists
        __ isDuplicate(currentFirst, mergedList) __ F..:
            # Place the node in sorted order
            sortNodeOrder(currentFirst, mergedList)
        currentFirst _ currentFirstNext
    # Insert list two into merged list
    _____ T..:
        __ currentSecond __ N..
            b..
        currentSecondNext _ currentSecond.n..
        currentSecond.n.. _ N..
        currentSecond.previous _ N..
        __ mergedList.head __ N..
            mergedList.head _ currentSecond
            currentSecond _ currentSecondNext
            c..
        # Check if node already exists
        __ isDuplicate(currentSecond, mergedList) __ F..:
            # Place the node in sorted order
            sortNodeOrder(currentSecond, mergedList)
        currentSecond _ currentSecondNext



linkedListOne _ LinkedList()
nodeOne _ Node(5)
nodeTwo _ Node(10)
nodeThree _ Node(7)
nodeFour _ Node(5)
linkedListOne.insertEnd(nodeOne)
linkedListOne.insertEnd(nodeTwo)
linkedListOne.insertEnd(nodeThree)
linkedListOne.insertEnd(nodeFour)

linkedListTwo _ LinkedList()
nodeFive _ Node(23)
nodeSix _ Node(7)
nodeSeven _ Node(1)
nodeEight _ Node(7)
linkedListTwo.insertEnd(nodeFive)
linkedListTwo.insertEnd(nodeSix)
linkedListTwo.insertEnd(nodeSeven)
linkedListTwo.insertEnd(nodeEight)


print("Printing List 1")
linkedListOne.printList()
print("Printing List 2")
linkedListTwo.printList()
print("Done")
mergedList _ LinkedList()
mergeList(linkedListOne, linkedListTwo, mergedList)

print("Printing Merged List")
mergedList.printList()
