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

    def -s
        s _ ""
        p _ head
        __ p !_ N.. :
                w__ p.next_node !_ N.. :
                        s +_ p.data
                        p _ p.next_node
                s +_ p.data
        r_ s


    def findElement  N
        __ head __ N..:
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

l.insert( 'a' )
l.insert( 'b' )
l.insert( 'c' )
l.insert( 'd' )
l.insert( 'e' )
l.insert( 'f' )
print l
print(l.findElement(3))

 
