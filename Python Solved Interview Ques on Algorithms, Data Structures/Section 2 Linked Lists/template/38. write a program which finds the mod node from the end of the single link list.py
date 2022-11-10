from pprint import pprint


class Node(object

    def  -  data_N.. next_node_None
        data _ data
        next_node _ N.. 

    def get_data
        r_  ?

    def get_next
        r_ next_node

    def set_next new_next
        next_node _ new_next

class LinkedList(object
    def  -  head_None
        head _ head

    def insert data
        new_node _ ? ?
        ?.set_next(head)
        head _ new_node

    def insertatEnd item
        current _ head
        __ ?
            w__ ?.g.. !_ N..:
                current _ ?.g..
            ?.s.. ? ?
        ____
            head _ ? ?


    def size
        current _ head
        count _ 0
        w__ ?
          count +_ 1
          current _ ?.g..
        r_ count 


    def modnodefromend  n
            current_head
            modnode_None
     
            i_1
            __ n <_ 0:
               r_ N..
     
            w__ current !_ N..:
                  __ i%n __ 0:
                       modnode_current
                  i_i+1
                  current_current.next_node
     
            r_ modnode





    def -s
        s _ ""
        p _ head
        __ p !_ N.. :
                w__ p.next_node !_ N.. :
                        s +_ p.data
                        p _ p.next_node
                s +_ p.data
        r_ s


l_ ?

l.insert( '250' )
l.insert( '200' )
l.insert( '100' )
l.insert( '25' )
l.insert( '20' )
l.insert( '10' )
print l
print(l.modnodefromend(3).data)
 
