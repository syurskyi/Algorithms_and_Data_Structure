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

    ___ deleteNode key
        temp _ head
        __(temp __ N..
            r_
        __(?.data __ key
            head _ ?.n..
            temp _ N..
            r_

        _____(?.n...data !_ key
            temp _ ?.n..

        target_node _ ?.n..
        ?.n.. _ target_node.n..
        target_node.n.. _ N..


# List Structure : 5 => 1 => 3 => 7
# 5 => 1 => 7
linked_list _ LinkedList()
linked_list.head _ Node(5)

second_node _ Node(1)
third_node _ Node(3)
fourth_node _ Node(7)

linked_list.head.n.. _ second_node
second_node.n.. _ third_node
third_node.n.. _ fourth_node

linked_list.deleteNode(3)
linked_list.printList()
