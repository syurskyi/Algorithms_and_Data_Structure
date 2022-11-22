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
            r_ Empty('Heap is empty')
        r_ _data[1]

    ___ insert e
        __ _currentsize __  maxsize:
            r_ Empty('No Space')
        _currentsize +_ 1
        i _ _currentsize
        while i!_ 1 and e < _data[i//2]:
            _data[i] _ _data[i//2]
            i _ i // 2
        _data[i] _ e

    ___ deletemin
        __ _currentsize __ 0:
            r_ Empty('Heap is Empty')
        x _ _data[1]
        y _ _data[_currentsize]
        _currentsize -_ 1
        i _ 1
        ci _ 2
        while ci <_ _currentsize:
            __ ci < _currentsize and _data[ci] > _data[ci+1]:
                ci +_ 1
            __ y <_ _data[ci]:
                break
            _data[i] _ _data[ci]
            i _ ci
            ci _ ci * 2
        _data[i] _ y
        r_ x


h _ ArrayHeap()
h.insert(25)
h.insert(14)
h.insert(2)
h.insert(20)
h.insert(10)
h.insert(12)
for i in range(h._currentsize):
    print(h.deletemin(), end_' , ')
