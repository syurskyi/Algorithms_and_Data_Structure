from pprint import pprint


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



    ___ deleteNode  position
      
             # If linked list is empty
             __ head __ N..:
                 r_
      
             # Store head node
             temp _ head
      
             # If head needs to be removed
             __ position __ 0:
                 head _ ?.next_node
                 temp _ N..
                 r_
      
             # Find previous node of the node to be deleted
             ___ i __ r..(position -1
                 temp _ ?.next_node
                 __ temp __ N..:
                     b..
      
             # If position is more than number of nodes
             __ temp __ N..:
                 r_
             __ ?.next_node __ N..:
                 r_
      
             # Node temp.next is the node to be deleted
             # store pointer to the next of node to be deleted
             next _ ?.next_node.next_node
      
             # Unlink the node from linked list
             ?.next_node _ N..
      
             ?.next_node _ next

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

l.deleteNode(2)
print l
l.deleteNode(1)
print l
l.deleteNode(0)
print l
