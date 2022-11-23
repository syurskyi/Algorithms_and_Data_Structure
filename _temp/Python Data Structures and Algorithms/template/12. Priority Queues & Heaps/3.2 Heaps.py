____ e.. _______ E..


c_ ArrayHeap:

    ___ -
        _maxsize _ 10
        _data _ [-1] * _maxsize
        _currentsize _ 0

    ___ -l
        r_ l.. ?

    ___ is_empty
        r_ l.. ?

    ___ maxh
        __ _currentsize __ 0:
            r_ ? 'Heap is empty')
        r_ _data[1]

    ___ insert e
        __ _currentsize __ _maxsize:
            r_ ? 'No Space')
        _currentsize +_ 1
        i _ _currentsize
        _____ i!_ 1 and e > _data[i//2]:
            _data[i] _ _data[i//2]
            i _ i // 2
        _data[i] _ e

    ___ deletemax
        __ _currentsize __ 0:
            r_ ? 'Heap is Empty')
        x _ _data[1]
        y _ _data[_currentsize]
        _currentsize -_ 1
        i _ 1
        ci _ 2
        _____ ci <_ _currentsize:
            __ ci < _currentsize and _data[ci] < _data[ci+1]:
                ci +_ 1
            __ y >_ _data[ci]:
                break
            _data[i] _ _data[ci]
            i _ ci
            ci _ ci * 2
            _data[i] _ y


h _ ArrayHeap()
h.i.. (25)
h.i.. (14)
h.i.. (2)
h.i.. (20)
h.i.. (10)
h.i.. (12)
print(h._data)
h.deletemax()
print(h._data)
