# Showing Memory Limit Exceeded only
# I hope it's OK

class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.arr = A
        self.countIdx = 0
        self.numIdx = 1

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        val = -1
        for _ in range(n):
            while self.countIdx < len(self.arr) and \
                    self.arr[self.countIdx] == 0:
                self.countIdx += 2
                self.numIdx += 2
            if self.countIdx >= len(self.arr):
                return -1
            val = self.arr[self.numIdx]
            self.arr[self.countIdx] -= 1
        return val


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
