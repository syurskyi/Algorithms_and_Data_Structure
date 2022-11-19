c_ Node o..

    ___  -  data_N.. next_node_None
        ? _ ?
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
            w__ ?.g.. !_ N..
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


___ divideListInto2(list1
  first_list1
  second_list1
  w__ first !_ N.. a__ first.next_node !_ N..
    second_second.next_node
    first_first.next_node
    first_first.next_node

  third _second.next_node
  second.next_node_None
  r_ list1, third

___ displayList(list1
  temp_list1
  w__ temp:
    print ?.data
    temp_temp.next_node


l_ ?

l.i.. ( 'a' )
l.i.. ( 'b' )
l.i.. ( 'c' )
l.i.. ( 'd' )
l.i.. ( 'e' )
l.i.. ( 'f' )
l.i.. ( 'g' )
print l
l1,l2_divideListInto2(l.head)
print "List1:"
displayList(l1)
print "List2:"
displayList(l2)
print "#####"
