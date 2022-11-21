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


    ___ search data
        current _ ?
        found _ F...
        w__ ? a__ ? __ F...
            __ ?.g.. __ ?
                f.. _ T..
            ____
                c.. _ ?.g..
        __ c.. __ N..
            r_ V..("Data not in list")
        r_ ?


    ___ delete data
        current _ ?
        previous _ N..
        found _ F...
        w__ ? a__ ? __ F...
            __ ?.g.. __ ?
                f.. _ T..
            ____
                p.. _ ?
                c.. _ ?.g..
        __ c.. __ N..
            r_ V..("Data not in list")
        __ ? __ N..
            h.. _ ?.g..
        ____
            previous.set_next(?.get_next())

    ___ -s
        s _ ""
        p _ head
        __ ? !_ N.. 
                w__ ?.n... !_ N.. :
                        ? +_ ?.d..
                        p _ ?.n...
                ? +_ ?.d..
        r_ s


    ___ findnthNodeFromEnd  n
      __ n < 0:
         r_ N..
      first_ head
      count _ 0
    
      w__ count < n a__ N.. !_ first:
        first_first.next_node
        count+_1
    
      __ count<n __ N..__first:
        r_ N..
    
      second_head
      w__ first.next_node !_ N..
        first_first.next_node
        second_second.next_node
 
      r_ second

l_ ?

l.i.. ( 'a' )
l.i.. ( 'b' )
l.i.. ( 'c' )

print l

print(l.findnthNodeFromEnd(0).data)
print(l.findnthNodeFromEnd(1).data)
print(l.findnthNodeFromEnd(2).data)
    

