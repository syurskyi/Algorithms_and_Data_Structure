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


    ___ search data
        current _ head
        found _ F...
        w__ current a__ found __ F...:
            __ ?.g.. __ data:
                found _ T..
            ____
                current _ ?.g..
        __ current __ N..:
            r_ V..("Data not in list")
        r_ ?


    ___ delete data
        current _ head
        previous _ N..
        found _ F...
        w__ current a__ found __ F...:
            __ ?.g.. __ data:
                found _ T..
            ____
                previous _ current
                current _ ?.g..
        __ current __ N..:
            r_ V..("Data not in list")
        __ previous __ N..:
            head _ ?.g..
        ____
            previous.set_next(?.get_next())

    ___ -s
        s _ ""
        p _ head
        __ p !_ N.. :
                w__ p.next_node !_ N.. :
                        s +_ p.data
                        p _ p.next_node
                s +_ p.data
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
      w__ first.next_node !_ N..:
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
    

