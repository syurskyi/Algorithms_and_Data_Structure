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

    ___ makeCycle
        current _ head
        __ ?
            w__ ?.g.. !_ N..:
                current _ ?.g..
            ?.next_node_head.next_node 

    ___ detectCycle
         first_head
         second_head

         loopLength _ 0
         w__(first a__ second
           first_first.g..
           __ (first  __ second
              r_ T..

           __ first __ N..:
              r_ F...  
 
           first _ first.g..
           __ (first __ second
              r_ T..

           second _ second.g..

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


l_ ?

l.i.. ( 'a' )
l.i.. ( 'b' )
l.i.. ( 'c' )

print l
l.makeCycle()
print(l.detectCycle())
