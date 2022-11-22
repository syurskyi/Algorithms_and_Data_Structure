from exceptions import Empty

class ArrayHeap:

    def __init__(self):
        self._maxsize = 10
        self._data = [-1] * self._maxsize
        self._currentsize = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data)

    def maxh(self):
        if self._currentsize == 0:
            raise Empty('Heap is empty')
        return self._data[1]

    def insert(self, e):
        if self._currentsize == self. maxsize:
            raise Empty('No Space')
        self._currentsize += 1
        i = self._currentsize
        while i!= 1 and e > self._data[i//2]:
            self._data[i] = self._data[i//2]
            i = i // 2
        self._data[i] = e

    def deletemax(self):
        if self._currentsize == 0:
            raise Empty('Heap is Empty')
        x = self._data[1]
        y = self._data[self._currentsize]
        self._currentsize -= 1
        i = 1
        ci = 2
        while ci <= self._currentsize:
            if ci < self._currentsize and self._data[ci] < self._data[ci+1]:
                ci += 1
            if y >= self._data[ci]:
                break
            self._data[i] = self._data[ci]
            i = ci
            ci = ci * 2
            self._data[i] = y


h = ArrayHeap()
h.insert(25)
h.insert(14)
h.insert(2)
h.insert(20)
h.insert(10)
h.insert(12)
print(h._data)
h.deletemax()
print(h._data)
