____ e.. _______ E..


c_ LinkedDeque:

    c_ _Node:
        __slots__ _ ' -element', ' -next'

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
        r_  size __ 0

    ___ add_first e
        newest _ _Node(e, None)
        __ ?
            _head _ newest
            _tail _ newest
        else:
            newest ._next _ _head
        _head _ newest
        _size +_ 1

    ___ add_last e
        newest _ _Node(e, None)
        __ ?
            _head _ newest
            _tail _ newest
        else:
            _tail._next _ newest
        _tail _ newest
        _size +_ 1

    ___ remove_first
        __ ?
            r_ Empty('Linked List Empty')
        value _ _head._element
        _head _ _head._next
        _size -_ 1

        __ ?
            _tail _ None
        r_ value

    ___ remove_last
        __ ?
            r_ Empty('Linked List Empty')
        thead _ _head
        i _ 0
        while i < l..(self) - 2:
            thead _ thead . next
            i +_ 1
        _tail _ thead
        thead _ thead._next
        value _ thead._element
        _tail._next _ None
        _size -_ 1
        r_ value

    ___ display
        thead _ _head
        while thead:
            print(thead._element, end_ '-->' )
            thead _ thead. next
        print()


L _ LinkedDeque()
L.add_last(10)
L.add_last(20)
L.add_last(30)
L.add_last(40)
L.display()
print('Deleted:', L.remove_first())
L.display()
L.add_first( 70)
L.display()
print('Deleted:', L.remove_last())
L.display()
