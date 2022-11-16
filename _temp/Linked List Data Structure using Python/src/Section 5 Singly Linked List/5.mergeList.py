from singlyLinkedList import Node, LinkedList

___ mergeLists(firstList, secondList, mergedList
    # 1->3->4 || 2->7->9 || 1->2->3->4->7->9->None
    currentFirst _ firstList.head
    currentSecond _ secondList.head
    _____ T..:
        __ currentFirst __ N..:
            mergedList.insertEnd(currentSecond)
            b..
        __ currentSecond __ N..:
            mergedList.insertEnd(currentFirst)
            b..
        __ currentFirst.data < currentSecond.data:
            currentFirstNext _ currentFirst.next
            currentFirst.next _ N..
            mergedList.insertEnd(currentFirst)
            currentFirst _ currentFirstNext
        ____
            currentSeconNext _ currentSecond.next
            currentSecond.next _ N..
            mergedList.insertEnd(currentSecond)
            currentSecond _ currentSeconNext


# First List
nodeOne _ Node(1)
nodeTwo _ Node(3)
nodeThree _ Node(4)
firstList _ LinkedList()
firstList.insertEnd(nodeOne)
firstList.insertEnd(nodeTwo)
firstList.insertEnd(nodeThree)

# Second List
nodeFour _ Node(2)
nodeFive _ Node(7)
nodeSix _ Node(9)
secondList _ LinkedList()
secondList.insertEnd(nodeFour)
secondList.insertEnd(nodeFive)
secondList.insertEnd(nodeSix)

print("Printing first list")
firstList.printList()
print("Printing second list")
secondList.printList()

mergedList _ LinkedList()

mergeLists(firstList, secondList, mergedList)
d.. firstList
d.. secondList

print("Printing Merged List")
mergedList.printList()
