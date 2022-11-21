c_ Node o..

    ___  -  data_N.. next_node_N..
        ? _ ?
        ? _ N..

    ___ get_data
        r_  ?

    ___ get_next
        r_ ?

    ___ set_next new_next
        next_node _ ?



c_ LinkedList o..
    ___  -  head_N...
        ? _ ?

    ___ i..  data
        new_node _ ? ?
        ?.s.. h..
        h.. _ ?

    ___ insertatEnd item
        current _ ?
        __ ?
            w__ ?.g.. !_ N..
                c.. _ ?.g..
            ?.s.. ? ?
        ____
            h.. _ ? ?

    ___ size
        current _ ?
        count _ 0
        w__ ?
          ? +_ 1
          c.. _ ?.g..
        r_ count


    ___ -s
        s _ ""
        p _ head
        __ ? !_ N.. 
                w__ ?.n... !_ N.. :
                        ? +_ ?.d..
                        p _ ?.n...
                ? +_ ?.d..
        r_ s


___ returnEnd(l
  l1_l.head 
  w__ ?.n... !_ N..
    l1_l1.next_node
  r_ l1

___ nodeJoiningPoint(list1, list2
  joiningPoint _     # dict
  t _ list1.head

  w__ t !_ N..
       joiningPoint[t]_True
       t_t.next_node

  t _ list2.head
  
  w__ t !_ N..
        __ joiningPoint.get(t) !_ N..
           r_ t
        t_t.next_node

  r_ N..

l1 _ LinkedList()
l2 _ LinkedList()

?.i.. ( 'a' )
?.i.. ( 'b' )
?.i.. ( 'c' )
print "list1:", l1
?.i.. ( '111' )
?.i.. ( '222' )
?.i.. ( '333' )
?.i.. ( '444' )
?.i.. ( '555' )
?.i.. ( '666' )
print "list2:", l2
l1lastNode_returnEnd(l1)
l2lastNode_returnEnd(l2)


l3_LinkedList()
l3.i.. ( 'ZZZ' )
l3.i.. ( 'YYY' )
l3.i.. ( 'XXX' )
print "list3:", l3

l1lastNode.next_node_l3.head
l2lastNode.next_node_l3.head
print l1
print l2

print (nodeJoiningPoint(l1, l2).data)
