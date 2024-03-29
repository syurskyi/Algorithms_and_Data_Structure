from pprint import pprint


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = None 

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insertatEnd(self,item):
        current = self.head
        if current:
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(Node(item))
        else:
            self.head = Node(item)


    def size(self):
        current = self.head
        count = 0
        while current:
          count += 1
          current = current.get_next()
        return count 


    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current


    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())



    def deleteNode(self, position):
      
             # If linked list is empty
             if self.head == None:
                 return
      
             # Store head node
             temp = self.head
      
             # If head needs to be removed
             if position == 0:
                 self.head = temp.next_node
                 temp = None
                 return
      
             # Find previous node of the node to be deleted
             for i in range(position -1 ):
                 temp = temp.next_node
                 if temp is None:
                     break
      
             # If position is more than number of nodes
             if temp is None:
                 return
             if temp.next_node is None:
                 return
      
             # Node temp.next is the node to be deleted
             # store pointer to the next of node to be deleted
             next = temp.next_node.next_node
      
             # Unlink the node from linked list
             temp.next_node = None
      
             temp.next_node = next

    def __str__( self ) :
        s = ""
        p = self.head
        if p != None :
                while p.next_node != None :
                        s += p.data
                        p = p.next_node
                s += p.data
        return s


l = LinkedList()

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
