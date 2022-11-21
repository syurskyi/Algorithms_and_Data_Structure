# c_ Node :
# 	___  - ? data )
# 		? _ ?
# 		n.. _ N..
# 		p.. _ N..
#
# c_ LinkedList
# 	___  -
# 		head _ N..
#
#         ___ insertAtBeg data
#                node _ ? ?
#                __ head __ N..
#                   h.. _ ?
#                ____
#                   ?.p___N..
#                   ?.n..
#                   ?.p..
#                   h.._n..
#
#
#         ___ insertAtEnd data
#               node_ ? ?
#               __ h.. __ N..
#                  h.. _ ?
#               ____
#                  current _ ?
#                  w__ ?.n.. !_ N..
#                        current_current.n..
#                  ?.n...
#                  ?.p..
#
#
#         ___ insertAtPos  pos, item
#                __ ? > size() __ ? < 0
#                    r_ N..
#                __ ? __ 0
#                    i.. ?
#                ____
#                    __ pos __ size(
#                        insertatEnd(item)
#                    ____
#                        newNode _ ? ?
#                        current _ ?
#                        count _ 0
#                        w__ count <_ pos - 1:
#                            ? +_ 1
#                            current _ ?.n..
#                        ?.prev_current.p..
#                        ?.p...next_newNode
#                        ?.next_current
#                        ?.prev_newNode
#
#
# #####     node1->node2->node3
# #####     if current node is node2
# #####     node1->newnode->node2->node3
# #                       newNode.prev=current.prev   ## if current node is node2, newnode.prev will be pointing to node1
# #                       current.prev.next=newNode   ##node1.next will be pointing to newnode
# #                       newNode.next=current        ##newnode.next will be pointing to node2
# #                       current.prev=newNode        ##node2.prev will be pointing to newnode
#
#
#
#
#         ___ search  k
#                p _ head
#                __ p __ n.. N..
#                    __ ?.data __ k:
#                        r_ p
#                    w__ ?.n.. __ n.. N..
#                        __ ?.data __ k:
#                            r_ p
#                        p _ ?.n..
#                r_ N..
#
#
# 	___ remove ? p ) :
# 		tmp _ ?.p..
# 		?.p...n.. _ ?.n..
# 		?.p.. _ tmp
#
#
#         ___ deleteatbeg
#               __ head __ n.. N..
#                  current _ ?
#                  head _ ?.n..
#
#         ___ deleteatpos  position
#
#              # If linked list is empty
#              __ head __ N..
#                  r_
#
#              # Store head node
#              t.. _ ?
#
#              # If head needs to be removed
#              __ position __ 0:
#                  head _ ?.n..
#                  t.. _ N..
#                  r_
#
#              # Find previous node of the node to be deleted
#              ___ i __ r.. ? -1
#                  temp _ ?.n..
#                  __ ? __ N..
#                      b..
#
#              # If position is more than number of nodes
#              __ ? __ N..
#                  r_
#              __ ?.n.. __ N..
#                  r_
#
#              # Node temp.next is the node to be deleted
#              # store pointer to the next of node to be deleted
#
# 	     ?.p...n.. _ ?.n..
# 	     ?.n...prev _ ?.p..
# 	     t.. _ N..
#
#         ___ deleteatend
#              __ head __ N..
#                 r_
#
#              current _ ?
#              w__ (?.n.. !_ N..
#                    current_current.n..
#
#              ?.p...next_None
#              current_None
#
#         ___ deleteatbeg
#              __ head __ N..
#                 r_
#
#              current _ ?
#              head _ head.n..
#              head.p.. _ N..
#              current _ N..
#
#         ___ size
#                current _ ?
#                count _ 0
#                w__ ?
#                  ? +_ 1
#                  current _ ?.n..
#                r_ count
#
#
# 	___ -s
# 		s _ ""
# 		p _ head
# 		__ ? !_ N..
# 			w__ ?.n.. !_ N.. :
# 				? +_ ?.d..
# 				p _ ?.n..
# 			? +_ ?.d..
# 		r_ s
#
# # example code
# l_ ?
#
# l.insertAtBeg( 'a' )
# print l
# print "inserting at beginning"
# l.insertAtBeg( 'b' )
# print l
# print "inserting at beginning"
# l.insertAtBeg( 'c' )
# print l
# print "inserting at end"
# l.insertAtEnd( 'd' )
# print l
# print "inserting at end"
# l.insertAtEnd( 'e' )
# print l
# print "inserting at end"
# l.insertAtEnd( 'f' )
# print l
# print "inserting at pos 1"
# l.insertAtPos(1,'ZZZZZ')
# print l
# print "inserting at pos 0"
# l.insertAtPos(0,'AAAAAAA')
# print l
# print "deleting at beginning"
# l.deleteatbeg()
# print l
# print "deleting at beginning"
# l.deleteatbeg()
# print l
# print "deleting at position 4 "
# l.deleteatpos(4)
# print l
# print "deleting at position 2"
# l.deleteatpos(2)
# print l
# print "deleting at end"
# l.deleteatend()
# print l
# print "deleting at beg"
# l.deleteatbeg()
# print l
