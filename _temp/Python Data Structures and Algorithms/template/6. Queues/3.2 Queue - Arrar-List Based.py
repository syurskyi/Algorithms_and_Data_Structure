____ e.. _______ E..


c_ ArrayQueue:
    ___ -
        _data _  # list
        _size _ 0
        _front _ 0

    ___ -l
        r_ _size

    ___ is_empty
        r_ _size

    ___ enqueue e
        ?.a.. ?
        _size _ _size + 1

    ___ dequeue
        __ ?
            r_ Empty('Queue is Empty')
        value _ _data[_front]
        _data[_front] _ None
        _front _ _front + 1
        _size _ _size - 1
        r_ value

    ___ first
        __ ?
            r_ Empty('Queue is Empty')
        r_ _data[_front]


q _ ArrayQueue()
q.enqueue(10)
q.enqueue(20)
print('Queue: ', q._data)
print('Length: ', l..(q))
# print( 'Dequeue: ' ,q.dequeue())
print( 'Queue: ', q._data)
q.enqueue(30)
q.enqueue(40)
print( 'Queue: ', q._data)
print( 'First Element: ', q.first())
print( 'Queue: ', q._data)
print( 'Dequeue: ', q.dequeue())
print( 'Queue: ', q._data)
