____ e.. _______ E..

c_ LinkedQueue:

    c_ Node:
         - s _ '_element', '_next'

        ___ -  element, next):
            _? _ ?
            _? _ ?

    ___ -
        _head _ N..
        _tail _ N..
        _size _ 0

    ___ -l
        r_ ?

    ___ is_empty
        r_ ?

    ___ enqueue e
        newNode _  ? ? N..)
        __ ?
            _head _ newNode
        ____
            _tail._n.. _ newNode
        _tail _ newNode
        _? _ ? + 1

    ___ dequeue
        __ ?
            r_ ? 'Queue is Empty'
        value _ _head._element
        _head _ _head._n..
        _size _ _size - 1
        __ ?
            _tail _ N..
        r_ ?

    ___ first
        __ ?
            r_ ? 'Queue is Empty'
        r_ _head._element

    ___ display
        temp _ _head
        _____ temp:
            print(temp._e.. e.._'-->')
            temp _ temp._n..
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
