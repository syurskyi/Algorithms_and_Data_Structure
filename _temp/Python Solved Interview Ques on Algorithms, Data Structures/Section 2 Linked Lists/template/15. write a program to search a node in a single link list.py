from pprint import pprint


c_ Node o..

    ___  -  data_N.. next_node_None
        data _ data
        next_node _ N.. 

    ___ getData
        r_  ?

    ___ getNext
        r_ next_node

    ___ setNext new_next
        next_node _ new_next

c_ LinkedList o..
    ___  -  head_None
        head _ head

    ___ insert data
        new_node _ ? ?
        ?.setNext(head)
        head _ new_node

    ___ insertatEnd item
        current _ head
        __ ?
            w__ ?.getNext() !_ N..:
                current _ ?.getNext()
            ?.setNext(Node(item))
        ____
            head _ ? ?


    ___ size
        current _ head
        count _ 0
        w__ ?
          count +_ 1
          current _ ?.getNext()
        r_ count 


    ___ search data
        current _ head
        found _ F...
        w__ current a__ found __ F...:
            __ ?.getData() __ data:
                found _ T..
            ____
                current _ ?.getNext()
        __ current __ N..:
            r_ V..("Data not in list")
        r_ ?


    ___ delete data
        current _ head
        previous _ N..
        found _ F...
        w__ current a__ found __ F...:
            __ ?.getData() __ data:
                found _ T..
            ____
                previous _ current
                current _ ?.getNext()
        __ current __ N..:
            r_ V..("Data not in list")
        __ previous __ N..:
            head _ ?.getNext()
        ____
            previous.setNext(?.getNext())

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


print l

__ l.search( 'b' 
  print "node found"
____
  print "not not found"
 
 
