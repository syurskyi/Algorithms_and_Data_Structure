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


def joinListsInSortedOrder(l1, l2
  thirdList_Node()
  parse_thirdList
  tempo_thirdList

  w__ l1 !_ N.. a__ l2 !_ N..:
    __ l1.data < l2.data:
      tempo.next_node_l1
      l1_l1.next_node
    ____
      tempo.next_node_l2
      l2_l2.next_node
    tempo_tempo.next_node

  __ l1 __ N..:
     tempo.next_node_l2

  __ l2 __ N..:
     tempo.next_node_l1

  w__ thirdList:
     __ thirdList.data:
       print thirdList.data
     thirdList_thirdList.next_node


l1 _ LinkedList()
l2 _ LinkedList()

l1.insert( '3' )
l1.insert( '2' )
l1.insert( '1' )
print "list1:", l1
l2.insert( '6' )
l2.insert( '5' )
l2.insert( '4' )
print "list2:", l2

joinListsInSortedOrder(l1.head, l2.head)

