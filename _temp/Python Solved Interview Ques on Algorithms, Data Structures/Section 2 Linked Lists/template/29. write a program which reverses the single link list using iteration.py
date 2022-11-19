c_ Node o..

    ___  -  data_N.. next_node_N..
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

    ___ reverseList
        last _ N..
        currentNode _ head

        w__(currentNode __ n.. N..
           next_currentNode.next_node
           currentNode.next_node_last
           last_currentNode
           currentNode_next

        head_last

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
l.i.. ( 'd' )
l.i.. ( 'e' )
l.i.. ( 'f' )
print l
l.reverseList()
print l
