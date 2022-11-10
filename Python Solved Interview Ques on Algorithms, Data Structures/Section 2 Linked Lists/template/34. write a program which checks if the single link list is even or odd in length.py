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


    def -s
        s _ ""
        p _ head
        __ p !_ N.. :
                w__ p.next_node !_ N.. :
                        s +_ p.data
                        p _ p.next_node
                s +_ p.data
        r_ s


def findLengthOfListEvenOdd(list1
  temp_list1
  w__ temp !_ N.. a__ temp.next_node !_ N..:
    temp _ temp.next_node.next_node
  __ temp __ N..:
    r_ 1
  r_ 0 
   


l_ ?

l.insert( 'a' )
l.insert( 'b' )
l.insert( 'c' )
l.insert( 'd' )
l.insert( 'e' )
l.insert( 'f' )
l.insert( 'g' )
l.insert( 'h' )
print l
__ findLengthOfListEvenOdd(l.head
  print "List is even in size"
____
  print "List is odd in size"
