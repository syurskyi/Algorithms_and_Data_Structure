c_ Node:

    ___ -  data
        ? _ ?
        n.. _ N..


c_ LinkedList

    ___ -  
        head _ N..

    ___ printList 
        temp _ head
        linked_list _ ""
        _____(temp
            linked_list +_ (s..(?.data) + " ")
            temp _ ?.n..
        print(linked_list)

    # list start at 0
    ___ insertNode val, pos
        target _ Node(val)
        __(pos __ 0
            target.n.. _ head
            head _ target
            r_

        ___ getPrev(pos
            temp _ head
            count _ 1
            _____(count < pos
                temp _ ?.n..
                count +_ 1
            r_ temp

        prev _ getPrev(pos)
        nextNode _ prev.n..

        prev.n.. _ target
        target.n.. _ nextNode


# List Structure : 5 => 1 => 3 => 7
linked_list _ LinkedList()
linked_list.head _ Node(5)

second_node _ Node(1)
third_node _ Node(3)
fourth_node _ Node(7)

linked_list.head.n.. _ second_node
second_node.n.. _ third_node
third_node.n.. _ fourth_node

linked_list.insertNode(2, 2)
linked_list.printList()
