
____ e.. _______ E..

c_ Doublylinkedlist:
    c_ _Node:
        __slots__ _ '_etement', '_prev', '_next'

        ___ -(self, element, prev, next):
            _element _ element
            _prev _ prev
            _next _ next

    ___ -
        _head _ _Node(None, None, None)
        _tail _ _Node(None, None, None)
        _head. next _ _tail
        _tail._prev _ _head
        _size _ 0

    ___ -l
        r_ _size

    ___ is_empty
        r_ _size __ 0

    ___ add_first e
        newest _ _Node(e, None, None)
        __ ?
            _head _ newest
            _tail _ newest
        else:
            newest._next _ _head
            _head._prev _ newest
        _head _ newest
        _size +_ 1

    ___ add_last e
        newest _ _Node(e, None, None)
        __ ?
            _head _ newest
            _tail _ newest
        else:
            _tail._next _ newest
            newest._prev _ _tail
        _tail _ newest
        _size +_ 1

    ___ add_any(self, e, pos):
        newest _ _Node(e, None, None)
        thead _ _head
        i _ 1
        while 1 < pos:
            thead _ thead._next
            i +_ 1
        newest._next _ thead._next
        thead._next _ newest
        thead._next._prev _ newest
        newest._prev _ thead
        _size +_ 1

    ___ remove_first
        __ ?
            r_ Empty('List is Empty')
        value _ _head._element
        _head _ _head._next
        _head._prev _ None
        _size -_ 1
        __ ?
            _tail _ None
        r_ value

    ___ remove_last
        __ ?
            r_ Empty('List is Empty')
        thead _ _head
        i _ 0
        while 1 < l..(self)-2:
            thead _ thead._next
            i +_ 1
        _tail _ thead
        thead _ thead._next
        value _ thead._element
        _tail._next _ None
        _size -_ 1
        r_ value

    ___ remove_any(self, pos):
        __ ?
            r_ Empty('List is Empty')
        thead _ _head
        i _ 1
        while 1 < pos-1:
            thead _ thead. next
            i +_ 1
        thead._next _ thead._next. next
        thead._next._next._prev _ thead
        _size -_ 1

    ___ display
        thead _ _head
        while thead:
            print(thead._element, end_'-->')
            thead _ thead. next
        print()


L _ Doublylinkedlist()
L.add_last(10)
L.add_last(20)
L.add_last(30)
L.add_last(40)
L. display()
print('Delete: ', L.remove_first())
L.display()
L.add_first(70)
L.display()
print('Delete: ', L.remove_last())
L.display()
L.add_any(100, 2)
L.display()
L.remove_any(2)
L.display()
