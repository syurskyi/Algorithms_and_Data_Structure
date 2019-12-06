class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None 
		self.prev = None  

class LinkedList :
	def __init__( self ) :
		self.head = None		

        def insertAtBeg(self, data):
               node = Node( data )
               if (self.head == None):
                  self.head = node 
               else:
                  node.prev=None
                  node.next=self.head
                  self.head.prev=node
                  self.head=node


        def insertAtEnd(self, data):
              node= Node(data)
              if (self.head == None):
                 self.head = node 
              else:
                 current = self.head
                 while (current.next != None):
                       current=current.next
                 current.next=node
                 node.prev=current


        def insertAtPos(self, pos, item):
               if pos > self.size() or pos < 0:
                   return None
               if pos == 0:
                   self.insertAtBeg(item)
               else:
                   if pos == self.size():
                       self.insertatEnd(item)
                   else:
                       newNode = Node(item)
                       current = self.head
                       count = 0
                       while count <= pos - 1:
                           count += 1
                           current = current.next
                       newNode.prev=current.prev
                       current.prev.next=newNode 
                       newNode.next=current
                       current.prev=newNode


#####     node1->node2->node3
#####     if current node is node2 
#####     node1->newnode->node2->node3    
#                       newNode.prev=current.prev   ## if current node is node2, newnode.prev will be pointing to node1
#                       current.prev.next=newNode   ##node1.next will be pointing to newnode
#                       newNode.next=current        ##newnode.next will be pointing to node2
#                       current.prev=newNode        ##node2.prev will be pointing to newnode
 



        def search(self, k):
               p = self.head
               if p is not None:
                   if p.data == k:
                       return p
                   while p.next is not None:
                       if p.data == k:
                           return p
                       p = p.next
               return None


	def remove( self, p ) :
		tmp = p.prev
		p.prev.next = p.next
		p.prev = tmp


        def deleteatbeg(self):
              if self.head is not None:
                 current = self.head
                 self.head = current.next

        def deleteatpos(self, position):

             # If linked list is empty
             if self.head == None:
                 return

             # Store head node
             temp = self.head

             # If head needs to be removed
             if position == 0:
                 self.head = temp.next
                 temp = None
                 return

             # Find previous node of the node to be deleted
             for i in range(position -1 ):
                 temp = temp.next
                 if temp is None:
                     break

             # If position is more than number of nodes
             if temp is None:
                 return
             if temp.next is None:
                 return

             # Node temp.next is the node to be deleted
             # store pointer to the next of node to be deleted
			 
	     temp.prev.next = temp.next
	     temp.next.prev = temp.prev
	     temp = None
			 
        def deleteatend(self):
             if self.head == None:
                return

             current = self.head
             while (current.next != None):
                   current=current.next
             
             current.prev.next=None
             current=None  

        def deleteatbeg(self):
             if self.head == None:
                return

             current = self.head
             self.head = self.head.next
             self.head.prev = None
             current = None 

        def size(self):
               current = self.head
               count = 0
               while current:
                 count += 1
                 current = current.next
               return count


	def __str__( self ) :
		s = ""
		p = self.head
		if p != None :		
			while p.next != None :
				s += p.data
				p = p.next
			s += p.data
		return s

# example code
l = LinkedList()

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
