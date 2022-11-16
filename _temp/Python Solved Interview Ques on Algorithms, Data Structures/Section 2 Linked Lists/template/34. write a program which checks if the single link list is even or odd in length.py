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


    ___ -s
        s _ ""
        p _ head
        __ p !_ N.. :
                w__ p.next_node !_ N.. :
                        s +_ p.data
                        p _ p.next_node
                s +_ p.data
        r_ s


___ findLengthOfListEvenOdd(list1
  temp_list1
  w__ temp !_ N.. a__ temp.next_node !_ N..:
    temp _ temp.next_node.next_node
  __ temp __ N..:
    r_ 1
  r_ 0 
   


l_ ?

l.i.. ( 'a' )
l.i.. ( 'b' )
l.i.. ( 'c' )
l.i.. ( 'd' )
l.i.. ( 'e' )
l.i.. ( 'f' )
l.i.. ( 'g' )
l.i.. ( 'h' )
print l
__ findLengthOfListEvenOdd(l.head
  print "List is even in size"
____
  print "List is odd in size"
