from pprint import pprint


c_ Node o..

    c_ -  data=None, next_node=None):
        ? ?
        ? ?

    c_ get_data(self):
        return self.data

    c_ get_next(self):
        return self.next_node

    c_ set_next(self, new_next):
        self.next_node = new_next

c_ LinkedList o..
    c_ -(self, head=None):
        self.head = head

    c_ insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    c_ insertatEnd(self,item):
        current = self.head
        if current:
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(Node(item))
        else:
            self.head = Node(item)

    c_ size(self):
        current = self.head
        count = 0
        while current:
          count += 1
          current = current.get_next()
        return count 


    c_ search(self, data):
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


    c_ delete(self, data):
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


    c_ deleteatbeg(self):
       if self.head is not None:
          current = self.head
          self.head = current.get_next()

    c_ __str__( self ) :
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
l.deleteatbeg() 
print l
l.deleteatbeg() 
print l
l.deleteatbeg() 
print l
 
