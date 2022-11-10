c_ Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next



c_ LinkedList(object):
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

    def __str__( self ) :
        s = ""
        p = self.head
        if p != None :
                while p.next_node != None :
                        s += p.data
                        p = p.next_node
                s += p.data
        return s


    def findnthNodeFromEnd(self, n):
      if n < 0:
         return None
      first= self.head
      count = 0
    
      while count < n and None != first:
        first=first.next_node
        count+=1
    
      if count<n or None==first:
        return None
    
      second=self.head
      while first.next_node != None:
        first=first.next_node
        second=second.next_node
 
      return second

l = LinkedList()

l.insert( 'a' )
l.insert( 'b' )
l.insert( 'c' )

print l

print(l.findnthNodeFromEnd(0).data)
print(l.findnthNodeFromEnd(1).data)
print(l.findnthNodeFromEnd(2).data)
    

