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

    def __str__( self ) :
        s = ""
        p = self.head
        if p != None :
                while p.next_node != None :
                        s += p.data
                        p = p.next_node
                s += p.data
        return s


    def findElement(self, N):
        if self.head == None:
            return None
        
        curNode = self.head
        num = 1 # number of elements in list
        while curNode.next_node:
            num += 1
            curNode = curNode.next_node
        
        if num < N or N <= 0: # list is too short
            return None
        
        # get num - N + 1 node
        curNode = self.head
        curNum  = 1
        while curNum < num - N + 1:
            curNum += 1
            curNode = curNode.next_node
        return curNode.data


l = LinkedList()

l.insert( 'a' )
l.insert( 'b' )
l.insert( 'c' )
l.insert( 'd' )
l.insert( 'e' )
l.insert( 'f' )
print l
print(l.findElement(3))

 
