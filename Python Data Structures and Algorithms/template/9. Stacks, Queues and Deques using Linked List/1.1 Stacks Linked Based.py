
from exceptions import Empty

class LinkedStack:
    class Node:
        __slots__ = '_element' , '_next'

        def __init__ (self, element, next):
            self._element = element
            self._next = next

    def __init__ (self):
        self._head = None
        self._size = 0

    def __len__ (self):
        return self._size

    def is_empty(self):
        return self. size == 0

    def push(self, e):
        self._head= self._Node(e,self._head)
        self._size= self._size+ 1

    def pop(self):
        if self.is_empty():
            raise Empty( 'Stack is Empty' )
        value= self._head._element
        self._head = self._head._next
        self._size = self._size - 1
        return value

    def top(self):
        if self.is_empty():
            raise Empty( 'Stack is Empty' )
        return self._head._element

    def display(self):
        temp= self._head
        while temp :
            print(temp._element, end= '-->' )
            temp= temp._next
        print()


ls= LinkedStack()
ls.push( 10)
ls.push( 20)

ls.push( 30)
ls.push(40 )
ls. display()
print( 'Popped: ', ls.pop())
ls. display()
ls.push( 70 )
ls.display()
print( 'Top Element: ', ls.top())
print( 'Popped: ' ,ls.pop())
ls.display()
