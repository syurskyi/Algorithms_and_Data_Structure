____ pprint ______ pprint


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


    ___ frNode
        fNode_None
        current_head
        i _ j _ 1
        
        w__ current !_ N..
            __ i __ j * j:
                __ fNode __ N..
                   fNode _ head
                ____
                   fNode _ fNode.next_node
                j _ j + 1
            i _ i + 1
            current_current.next_node

        print fNode.data 
         

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
print l
l.frNode()

 
