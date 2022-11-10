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

    ___ insert data
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
                w__ p.next_node !_ N.. :
                        s +_ p.data
                        p _ p.next_node
                s +_ p.data
        r_ s


___ returnEnd(l
  l1_l.head 
  w__ l1.next_node !_ N..:
    l1_l1.next_node
  r_ l1

___ nodeJoiningPoint(list1, list2
  joiningPoint _ {}
  t _ list1.head

  w__ t !_ N..:
       joiningPoint[t]_True
       t_t.next_node

  t _ list2.head
  
  w__ t !_ N..:
        __ joiningPoint.get(t) !_ N..:
           r_ t
        t_t.next_node

  r_ N..

l1 _ LinkedList()
l2 _ LinkedList()

l1.insert( 'a' )
l1.insert( 'b' )
l1.insert( 'c' )
print "list1:", l1
l2.insert( '111' )
l2.insert( '222' )
l2.insert( '333' )
l2.insert( '444' )
l2.insert( '555' )
l2.insert( '666' )
print "list2:", l2
l1lastNode_returnEnd(l1)
l2lastNode_returnEnd(l2)


l3_LinkedList()
l3.insert( 'ZZZ' )
l3.insert( 'YYY' )
l3.insert( 'XXX' )
print "list3:", l3

l1lastNode.next_node_l3.head
l2lastNode.next_node_l3.head
print l1
print l2

print (nodeJoiningPoint(l1, l2).data)
