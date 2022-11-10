from pprint import pprint


c_ Node(object

    def  -  data_N.. next_node_None
        data _ data
        next_node _ N.. 

    def get_data
        r_  ?

    def get_next
        r_ next_node

    def set_next new_next
        next_node _ new_next

c_ LinkedList(object
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


    def search data
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


    def delete data
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



    def deleteNode  position
      
             # If linked list is empty
             __ head __ N..:
                 r_
      
             # Store head node
             temp _ head
      
             # If head needs to be removed
             __ position __ 0:
                 head _ temp.next_node
                 temp _ N..
                 r_
      
             # Find previous node of the node to be deleted
             for i in range(position -1 
                 temp _ temp.next_node
                 __ temp __ N..:
                     break
      
             # If position is more than number of nodes
             __ temp __ N..:
                 r_
             __ temp.next_node __ N..:
                 r_
      
             # Node temp.next is the node to be deleted
             # store pointer to the next of node to be deleted
             next _ temp.next_node.next_node
      
             # Unlink the node from linked list
             temp.next_node _ N..
      
             temp.next_node _ next

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

l.insert( 'a' )
l.insert( 'b' )
l.insert( 'c' )

print l

l.deleteNode(2)
print l
l.deleteNode(1)
print l
l.deleteNode(0)
print l
