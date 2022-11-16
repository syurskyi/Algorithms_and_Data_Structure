c_ Node :
	___  -( self, data ) :
		data _ data
		next _ N.. 
		prev _ N..  

c_ LinkedList :
	___  -
		head _ N..		

        ___ insertAtBeg data
               node _ Node( data )
               __ (head __ N..
                  head _ node 
               ____
                  node.prev_None
                  node.next_head
                  head.prev_node
                  head_node


        ___ insertAtEnd data
              node_ ? ?
              __ (head __ N..
                 head _ node 
              ____
                 current _ head
                 w__ (?.next !_ N..
                       current_current.next
                 ?.next_node
                 node.prev_current


        ___ insertAtPos  pos, item
               __ pos > size() __ pos < 0:
                   r_ N..
               __ pos __ 0:
                   insertAtBeg(item)
               ____
                   __ pos __ size(
                       insertatEnd(item)
                   ____
                       newNode _ ? ?
                       current _ head
                       count _ 0
                       w__ count <_ pos - 1:
                           count +_ 1
                           current _ ?.next
                       newNode.prev_current.prev
                       ?.prev.next_newNode 
                       newNode.next_current
                       ?.prev_newNode


#####     node1->node2->node3
#####     if current node is node2 
#####     node1->newnode->node2->node3    
#                       newNode.prev=current.prev   ## if current node is node2, newnode.prev will be pointing to node1
#                       current.prev.next=newNode   ##node1.next will be pointing to newnode
#                       newNode.next=current        ##newnode.next will be pointing to node2
#                       current.prev=newNode        ##node2.prev will be pointing to newnode
 



        ___ search  k
               p _ head
               __ p __ n.. N..:
                   __ p.data __ k:
                       r_ p
                   w__ p.next __ n.. N..:
                       __ p.data __ k:
                           r_ p
                       p _ p.next
               r_ N..


	___ remove( self, p ) :
		tmp _ p.prev
		p.prev.next _ p.next
		p.prev _ tmp


        ___ deleteatbeg
              __ head __ n.. N..:
                 current _ head
                 head _ ?.next

        ___ deleteatpos  position

             # If linked list is empty
             __ head __ N..:
                 r_

             # Store head node
             temp _ head

             # If head needs to be removed
             __ position __ 0:
                 head _ temp.next
                 temp _ N..
                 r_

             # Find previous node of the node to be deleted
             ___ i __ r..(position -1 
                 temp _ temp.next
                 __ temp __ N..:
                     b..

             # If position is more than number of nodes
             __ temp __ N..:
                 r_
             __ temp.next __ N..:
                 r_

             # Node temp.next is the node to be deleted
             # store pointer to the next of node to be deleted
			 
	     temp.prev.next _ temp.next
	     temp.next.prev _ temp.prev
	     temp _ N..
			 
        ___ deleteatend
             __ head __ N..:
                r_

             current _ head
             w__ (?.next !_ N..
                   current_current.next
             
             ?.prev.next_None
             current_None  

        ___ deleteatbeg
             __ head __ N..:
                r_

             current _ head
             head _ head.next
             head.prev _ N..
             current _ N.. 

        ___ size
               current _ head
               count _ 0
               w__ ?
                 count +_ 1
                 current _ ?.next
               r_ count


	___ -s
		s _ ""
		p _ head
		__ p !_ N.. :		
			w__ p.next !_ N.. :
				s +_ p.data
				p _ p.next
			s +_ p.data
		r_ s

# example code
l_ ?

l.insertAtBeg( 'a' )
print l
print "inserting at beginning"
l.insertAtBeg( 'b' )
print l
print "inserting at beginning"
l.insertAtBeg( 'c' )
print l
print "inserting at end"
l.insertAtEnd( 'd' )
print l
print "inserting at end"
l.insertAtEnd( 'e' )
print l
print "inserting at end"
l.insertAtEnd( 'f' )
print l
print "inserting at pos 1"
l.insertAtPos(1,'ZZZZZ')
print l
print "inserting at pos 0"
l.insertAtPos(0,'AAAAAAA')
print l
print "deleting at beginning"
l.deleteatbeg()
print l
print "deleting at beginning"
l.deleteatbeg()
print l
print "deleting at position 4 "
l.deleteatpos(4)
print l
print "deleting at position 2"
l.deleteatpos(2)
print l
print "deleting at end"
l.deleteatend()
print l
print "deleting at beg"
l.deleteatbeg()
print l
