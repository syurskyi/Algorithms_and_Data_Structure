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


def joinListsInSortedOrder(l1, l2):
  thirdList=Node()
  parse=thirdList
  tempo=thirdList

  while l1 != None and l2 != None:
    if l1.data < l2.data:
      tempo.next_node=l1
      l1=l1.next_node
    else:
      tempo.next_node=l2
      l2=l2.next_node
    tempo=tempo.next_node

  if l1 == None:
     tempo.next_node=l2

  if l2 == None:
     tempo.next_node=l1

  while thirdList:
     if thirdList.data:
       print thirdList.data
     thirdList=thirdList.next_node


l1 = LinkedList()
l2 = LinkedList()

l1.insert( '3' )
l1.insert( '2' )
l1.insert( '1' )
print "list1:", l1
l2.insert( '6' )
l2.insert( '5' )
l2.insert( '4' )
print "list2:", l2

joinListsInSortedOrder(l1.head, l2.head)

