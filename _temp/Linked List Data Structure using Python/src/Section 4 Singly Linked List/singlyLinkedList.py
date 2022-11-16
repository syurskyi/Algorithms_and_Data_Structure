# Create nodes
# Create linked list
# Add nodes to linked list
# Print linked list

c_ Node:
    ___ -  data
        data _ data
        next _ N..

c_ LinkedList:
    ___ -  
        head _ N..

    ___ insert newNode
        # head=>John->None
        __ head __ N..:
            head _ newNode
        ____
            # head=>John->Ben->None || John -> Matthew
            lastNode _ head
            _____ True:
                __ lastNode.next __ N..:
                    break
                lastNode _ lastNode.next
            lastNode.next _ newNode

    ___ printList 
        # head => John -> Ben -> Matthew -> None
        __ head __ N..:
            print("List is empty")
            r_
        currentNode _ head
        _____ True:
            __ currentNode __ N..:
                break
            print(currentNode.data)
            currentNode _ currentNode.next


# Node => data, next
# firstNode.data => John, firstNode.next => None
firstNode _ Node("John")
linkedList _ LinkedList()
linkedList.insert(firstNode)
secondNode _ Node("Ben")
linkedList _ LinkedList()
linkedList.insert(secondNode)
thirdNode _ Node("Matthew")
linkedList.insert(thirdNode)
linkedList.printList()

