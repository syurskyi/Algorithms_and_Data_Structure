____ pprint ______ pprint


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
        r_ ?


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


    ___ findElement  N
        __ head __ N..
            r_ N..
        
        curNode _ head
        num _ 1 # number of elements in list
        w__ curNode.next_node:
            num +_ 1
            curNode _ curNode.next_node
        
        __ num < N __ N <_ 0: # list is too short
            r_ N..
        
        # get num - N + 1 node
        curNode _ head
        curNum  _ 1
        w__ curNum < num - N + 1:
            curNum +_ 1
            curNode _ curNode.next_node
        r_ curNode.data


l_ ?

l.i.. ( 'a' )
l.i.. ( 'b' )
l.i.. ( 'c' )
l.i.. ( 'd' )
l.i.. ( 'e' )
l.i.. ( 'f' )
print l
print(l.findElement(3))

 
