from pprint import pprint


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = None 

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

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

    def insertAtPos(self, pos, item):
        if pos > self.size() or pos < 0:
            return None
        if pos == 0:
            self.insert(item)
        else:
            if pos == self.size():
                self.insertatEnd(item)
            else:
                newNode = Node(item)
                newNode.set_data(item)
                current = self.head
                count = 0
                while count < pos - 1:
                    count += 1
                    current = current.get_next()
                newNode.set_next(current.get_next())
                current.set_next(newNode)

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

l.insertatEnd( 'a' )
l.insertatEnd( 'b' )
l.insertatEnd( 'c' )

print l

l.insertAtPos(1,'ZZZZZ')

print l

#if l.search( 'b' ):
#  print "node found"
#else:
#  print "not not found"
# 
#l.delete( 'b' ) 
#print l
# 
