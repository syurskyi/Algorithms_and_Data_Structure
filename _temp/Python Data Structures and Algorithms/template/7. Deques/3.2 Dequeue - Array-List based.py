____ e.. _______ E..

c_ ArrayDeque:
    ___ -
        _data _  # list
        _front _ 0

    ___ -l
        r_ l.. ?

    ___ is_empty
        r_ l.. ? __ 0

    ___ first
        __ ?
            r_ Empty('Deque is Empty')
        r_ _data[_front]

    ___ add_first e
        ?.insert(_front, e)

    ___ add_last e
        ?.a.. ?

    ___ delete_first
        __ ?
            r_ Empty('Deque is Empty')
        value _ ?.pop(_front)
        r_ value

    ___ delete_last
        __ ?
            r_ Empty('Deque is Empty')
        value _ ?.p..
        r_ value


d _ ArrayDeque()
d.add_last(10)
d.add_last(20)
d.add_last(30)
d.add_last(40)
d.add_last(50)
print('Deque: ', d._data)
print('Detete First: ', d.delete_first())
print('Deque: ', d._data)
print('Detete Last: ', d.delete_last())
print('Deque: ', d._data)
d.add_first(50)
print( 'Deque: ', d._data)
d.add_last( 60)
print( 'Deque: ', d._data)
print ( 'Length: ', l..(d))