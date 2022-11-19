c_ Node o..

    ___  -  data_N.. next_node_None
        data _ data
        next_node _ N..

    ___ get_data
        r_  ?

    ___ get_next
        r_ next_node

    ___ set_next new_next
        next_node _ new_next



c_ LinkedList o..
    ___  -  head_None
        head _ head

    ___ i..  data
        new_node _ ? ?
        ?.s.. h..
        head _ new_node

    ___ insertatEnd item
        current _ head
        __ ?
            w__ ?.g.. !_ N..:
                current _ ?.g..
            ?.s.. ? ?
        ____
            head _ ? ?

    ___ size
        current _ head
        count _ 0
        w__ ?
          count +_ 1
          current _ ?.g..
        r_ count


    ___ -s
        s _ ""
        p _ head
        __ p !_ N.. :
                w__ ?.next_node !_ N.. :
                        s +_ ?.data
                        p _ ?.next_node
                s +_ ?.data
        r_ s


___ joinListsInSortedOrder(l1, l2
  thirdList_Node()
  parse_thirdList
  tempo_thirdList

  w__ l1 !_ N.. a__ l2 !_ N..:
    __ l1.data < l2.data:
      tempo.next_node_l1
      l1_l1.next_node
    ____
      tempo.next_node_l2
      l2_l2.next_node
    tempo_tempo.next_node

  __ l1 __ N..:
     tempo.next_node_l2

  __ l2 __ N..:
     tempo.next_node_l1

  w__ thirdList:
     __ thirdList.data:
       print thirdList.data
     thirdList_thirdList.next_node


l1 _ LinkedList()
l2 _ LinkedList()

l1.i.. ( '3' )
l1.i.. ( '2' )
l1.i.. ( '1' )
print "list1:", l1
l2.i.. ( '6' )
l2.i.. ( '5' )
l2.i.. ( '4' )
print "list2:", l2

joinListsInSortedOrder(l1.head, l2.head)

