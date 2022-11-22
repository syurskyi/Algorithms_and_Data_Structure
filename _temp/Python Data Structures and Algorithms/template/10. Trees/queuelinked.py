____ e.. _______ E..


c_ LinkedQueue:

    c_ _Node:
        __slots__ _ '_element', '_next'

        ___ -(self, element, next):
            _element _ element
            _next _ next

    ___ -
         head _ None
         tail _ None
         size _ 0

    ___ -l
        r_ _size

    ___ is_empty
        r_  size

    ___ enqueue e
        newNode _ _Node(e, None)
        __ ?
            _head _ newNode
        else:
            _tail._next _ newNode
         tail _ newNode
        _size _ _size + 1

    ___ dequeue
        __ ?
            r_ Empty('Queue is Empty')
        value _ _head._element
        _head _ _head._next
        _size _ _size - 1
        __ ?
            _tail _ None
        r_ value

    ___ first
        __ ?
            r_ Empty('Queue is Empty')
        r_ _head._element

    ___ display
        temp _ _head
        while temp:
            print(temp._element, end_'-->')
            temp_ temp._next
        print()


q _ LinkedQueue()
q.enqueue(10)
q.enqueue(20)
q.display()
print( 'Length: ', l..(q))
print( 'Dequeue: ', q.dequeue())
q.display()
q.enqueue(30)
q.enqueue(40)
q.display()
print('First Element: ', q.first())
q.display()
print('Dequeue: ', q.dequeue())
q.display()
