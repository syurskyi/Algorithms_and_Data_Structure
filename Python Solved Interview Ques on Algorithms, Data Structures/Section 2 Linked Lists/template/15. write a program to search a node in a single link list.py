from pprint import pprint


c_ Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = None 

    def getData(self):
        return self.data

    def getNext(self):
        return self.next_node

    def setNext(self, new_next):
        self.next_node = new_next

c_ LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node

    def insertatEnd(self,item):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))
        else:
            self.head = Node(item)


    def size(self):
        current = self.head
        count = 0
        while current:
          count += 1
          current = current.getNext()
        return count 


    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        if current is None:
            raise ValueError("Data not in list")
        return current


    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

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

if l.search( 'b' ):
  print "node found"
else:
  print "not not found"
 
 
