
____ e.. _______ E..

c_ Circularlinkedlist:

    c_ _Node:

        __slots__ _ '_element', '_next'

        ___ -(self, element, next):
            _element _ element
            _next _ next

    ___ -
        _head _ None
        _tail _ None
        _size _ 0

    ___ -l
        r_ _size

    ___ is_empty
        r_ _size

    ___ add_first e
        newest _ _Node(e, None)
        __ ?
            newest._next _ newest
            _head _ newest
            _tail _ newest
        else:
            _tail._next _ newest
            newest._next _ _head
            _head _ newest
            _size +_ 1

    ___ add_last e
        newest _ _Node(e, None)
        __ ?
            _head _ newest
            newest._next _ newest
        else:
            newest._next _  tail. next
            _tail._next _ newest
        _tail _ newest
        _size +_ 1

    ___ add_any(self, e, pos):
        newest _ _Node(e, None)
        thead _ _head
        i _ 1
        while 1 < pos:
            thead _ thead._next
            i +_ 1
        newest._next _ thead._next
        thead._next _ newest
        _size +_ 1

    ___ remove_first
        __ ?
            r_ Empty('Linked List Empty')
        oldhead _ _tail._next
        _tail._next _ oldhead._next
        _head _ oldhead._next
        _size -_ 1
        __ ?
            _tail _ None
        r_ oldhead._element

    ___ remove_last
        __ ?
            r_ Empty('Linked List Empty')
        thead _ _head
        i _ 0
        while i < l..(self) - 2:
            thead _ thead._next
            i +_ 1
        _tail _ thead
        thead _ thead._next
        _tail._next _ _head
        value _ thead._element
        _size -_ 1
        r_ value

    ___ remove_any(self, pos):
        __ ?
            r_ Empty('Linked List Empty')
        thead _ _head
        i _ 1
        while i < pos-1:
            thead _ thead. next
            i +_ 1
        value _ thead._next._element
        thead._next _ thead._next._next
        _size -_ 1
        r_ value

    ___ display

        thead _ _head
        i _ 0
        while i < l..
            print(thead._element, end_'-->')
            thead _ thead._next
            i +_ 1
        print()


CL_ Circularlinkedlist()
CL.add_last( 10)
CL.add_last( 20)
CL.add_last(30)
CL.add_last(40)
CL.display()
print('Deteted: ', CL.remove_first())
CL.display()
CL.add_first(70)
CL.display()
print('Deteted: ', CL.remove_last())
CL.display()
CL.add_last(80)
CL.display()
