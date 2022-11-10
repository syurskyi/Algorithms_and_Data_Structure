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

    def makeCycle(self):
        current = self.head
        if current:
            while current.get_next() != None:
                current = current.get_next()
            current.next_node=self.head.next_node 

    def findTheStartNodeOfLoop(self):
         first=self.head
         second=self.head.next_node

         while second != first:
           second = second.next_node
           first = first.next_node.next_node
           if (first == None):
              return None

         second=self.head
         while second != first:
           second = second.next_node
           first = first.next_node

         return second

    def size(self):
        current = self.head
        count = 0
        while current:
          count += 1
          current = current.get_next()
        return count



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
l.makeCycle()
print(l.findTheStartNodeOfLoop().data)
