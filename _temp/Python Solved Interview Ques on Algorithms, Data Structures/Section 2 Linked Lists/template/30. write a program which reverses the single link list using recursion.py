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

    ___ reverse  node
       __ node.next_node __ N..:
           head _ node
           r_
       reverse(node.next_node)
       temp _ node.next_node
       temp.next_node_node
       node.next_node_None

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


l_ ?

l.insert( 'a' )
l.insert( 'b' )
l.insert( 'c' )
l.insert( 'd' )
l.insert( 'e' )
l.insert( 'f' )
print l
l.reverse(l.head)
print l
