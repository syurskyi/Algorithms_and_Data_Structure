c_ Node:
    ___ -  data
        data _ data
        prev _ N..
        next _ N..


c_ LinkedList:
    ___ -  
        head _ N..

    ___ createList arr
        start _ head
        n _ l..(arr)

        temp _ start
        i _ 0

        _____(i < n
            newNode _ Node(arr[i])
            __(i __ 0
                start _ newNode
                temp _ start
            ____
                ?.next _ newNode
                newNode.prev _ temp
                temp _ ?.next
            i +_ 1
        head _ start
        r_ start

    ___ printList 
        temp _ head
        linked_list _ ""
        _____(temp
            linked_list +_ (str(?.data) + " ")
            temp _ ?.next

        print(linked_list)

    ___ countList 
        temp _ head
        count _ 0
        _____(temp __ n.. N..
            temp _ ?.next
            count +_ 1
        r_ count

    # we will consider that the index begin at 1
    ___ insertAtLocation value, index
        temp _ head

        count _ countList()

        #index is 6, count is 5, valid 
        #index is 7, count is 5, 
        __(count+1<index
            r_ temp
        
        newNode _ Node(value)

        __(index __ 1
            newNode.next _ temp
            ?.prev _ newNode
            head _ newNode
            r_ head
        
        __(index __ count +1
            _____(?.next __ n.. N..
                temp _ ?.next

            ?.next _ newNode
            newNode.prev _ temp
            r_ head
        
        i _ 1
        _____(i < index-1
            temp _ ?.next
            i+_1
        
        nodeAtTarget _ ?.next

        newNode.next _ nodeAtTarget
        nodeAtTarget.prev _ newNode

        ?.next _ newNode
        newNode.prev _ temp

        r_ head


arr _ [1, 2, 3, 4, 5]

llist _ LinkedList()

llist.createList(arr)

llist.insertAtLocation(5,6)

llist.printList()
