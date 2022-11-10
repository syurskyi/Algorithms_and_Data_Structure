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

    def __str__( self ) :
        s = ""
        p = self.head
        if p != None :
                while p.next_node != None :
                        s += p.data
                        p = p.next_node
                s += p.data
        return s


def divideListInto2(list1):
  first=list1
  second=list1
  while first != None and first.next_node != None:
    second=second.next_node
    first=first.next_node
    first=first.next_node

  third =second.next_node
  second.next_node=None
  return list1, third

def displayList(list1):
  temp=list1
  while temp:
    print temp.data
    temp=temp.next_node


l = LinkedList()

l.insert( 'a' )
l.insert( 'b' )
l.insert( 'c' )
l.insert( 'd' )
l.insert( 'e' )
l.insert( 'f' )
l.insert( 'g' )
print l
l1,l2=divideListInto2(l.head)
print "List1:"
displayList(l1)
print "List2:"
displayList(l2)
print "#####"
