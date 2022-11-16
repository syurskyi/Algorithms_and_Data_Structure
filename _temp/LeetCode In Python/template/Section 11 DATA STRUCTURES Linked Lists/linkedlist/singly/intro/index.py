c_ Node:
    ___ -  data
        data _ data
        next _ N..


c_ LinkedList:
    ___ -
        head _ N..

    ___ printList
        temp _ head
        linked_list _ ""
        _____(temp
            linked_list +_ (str(temp.data) + " ")
            temp _ temp.next
        print(linked_list)

# Node strucutre: 5 => 1 => 3 => 7


linked_list _ LinkedList()
linked_list.head _ Node(5)

second_node _ Node(1)
third_node _ Node(3)
fourth_node _ Node(7)

linked_list.head.next _ second_node
second_node.next _ third_node
third_node.next _ fourth_node

linked_list.printList()
