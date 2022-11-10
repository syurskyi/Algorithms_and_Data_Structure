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


def returnEnd(l):
  l1=l.head 
  while l1.next_node != None:
    l1=l1.next_node
  return l1

def nodeJoiningPoint(list1, list2):
  joiningPoint = {}
  t = list1.head

  while t != None:
       joiningPoint[t]=True
       t=t.next_node

  t = list2.head
  
  while t != None:
        if joiningPoint.get(t) != None:
           return t
        t=t.next_node

  return None

l1 = LinkedList()
l2 = LinkedList()

l1.insert( 'a' )
l1.insert( 'b' )
l1.insert( 'c' )
print "list1:", l1
l2.insert( '111' )
l2.insert( '222' )
l2.insert( '333' )
l2.insert( '444' )
l2.insert( '555' )
l2.insert( '666' )
print "list2:", l2
l1lastNode=returnEnd(l1)
l2lastNode=returnEnd(l2)


l3=LinkedList()
l3.insert( 'ZZZ' )
l3.insert( 'YYY' )
l3.insert( 'XXX' )
print "list3:", l3

l1lastNode.next_node=l3.head
l2lastNode.next_node=l3.head
print l1
print l2

print (nodeJoiningPoint(l1, l2).data)
