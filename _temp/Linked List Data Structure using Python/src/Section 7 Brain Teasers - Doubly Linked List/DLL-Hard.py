# Merge two unsorted list into a sorted list such that final list has no duplicate values

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

    ___ printList 
        __ head __ N..:
            print("Empty list")
            r_
        currentNode _ head
        _____ T..:
            print(currentNode.data)
            __ currentNode.next __ N..:
                break
            currentNode _ currentNode.next

___ isDuplicate(currentNode, mergedList
    currentMerge _ mergedList.head
    # Check if data already exists in list
    _____ currentMerge __ n.. N..:
        __ currentNode.data __ currentMerge.data:
            r_ T..
        currentMerge _ currentMerge.next
    r_ F..

___ sortNodeOrder(currentNode, mergedList
    currentMerge _ mergedList.head
    _____ T..:
        # Insert in sorted order
        __ currentNode.data < currentMerge.data:
            # Check if currentNode is to be made the new head node
            __ currentMerge __ mergedList.head:
                currentNode.next _ currentMerge
                currentMerge.previous _ currentNode
                mergedList.head _ currentNode
            ____
                currentNode.previous _ currentMerge.previous
                currentNode.next _ currentMerge
                currentMerge.previous.next _ currentNode
                currentMerge.previous _ currentNode
            r_
        ____
            __ currentMerge.next __ N..:
                currentMerge.next _ currentNode
                currentNode.previous _ currentMerge
                r_
            currentMerge _ currentMerge.next

___ mergeList(linkedListOne, linkedListTwo, mergedList
    currentFirst _ linkedListOne.head
    currentSecond _ linkedListTwo.head
    # Insert list one into merged list
    _____ T..:
        __ currentFirst __ N..:
            break
        currentFirstNext _ currentFirst.next
        currentFirst.next _ N..
        currentFirst.previous _ N..
        __ mergedList.head __ N..:
            mergedList.head _ currentFirst
            currentFirst _ currentFirstNext
            continue
        # Check if node already exists
        __ isDuplicate(currentFirst, mergedList) __ F..:
            # Place the node in sorted order
            sortNodeOrder(currentFirst, mergedList)
        currentFirst _ currentFirstNext
    # Insert list two into merged list
    _____ T..:
        __ currentSecond __ N..:
            break
        currentSecondNext _ currentSecond.next
        currentSecond.next _ N..
        currentSecond.previous _ N..
        __ mergedList.head __ N..:
            mergedList.head _ currentSecond
            currentSecond _ currentSecondNext
            continue
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
