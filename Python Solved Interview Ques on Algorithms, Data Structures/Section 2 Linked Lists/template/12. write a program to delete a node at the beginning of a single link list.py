from pprint import pprint


c_ Node o..

    c_ -  data_N.. next_node_None
        ? ?
        ? ?

    c_ get_data
        r_  ?

    c_ get_next
        r_ next_node

    c_ set_next new_next
        next_node _ new_next

c_ LinkedList o..
    c_ -  head_None
        head _ head

    c_ insert data
        new_node _ ? ?
        ?.set_next(head)
        head _ new_node

    c_ insertatEnd item
        current _ head
        __ ?
            w__ ?.g.. !_ N..:
                current _ ?.g..
            ?.s.. ? ?
        ____
            head _ ? ?

    c_ size
        current _ head
        count _ 0
        w__ ?
          count +_ 1
          current _ ?.g..
        r_ count 


    c_ search data
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


    c_ delete data
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


    c_ deleteatbeg
       __ head __ not N..:
          current _ head
          head _ ?.g..

    c_ -s
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
print l
l.deleteatbeg() 
print l
l.deleteatbeg() 
print l
l.deleteatbeg() 
print l
 
