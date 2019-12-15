'''
Created on Sep 11, 2019

@author: tongq
'''
import bisect
class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.rowNum = N
        self.l = []

    def seat(self):
        """
        :rtype: int
        """
        if not self.l:
            res = 0
        else:
            d, res = self.l[0], 0
            for a, b in zip(self.l, self.l[1:]):
                if (b-a)//2 > d:
                    d, res = (b-a)//2, (b+a)//2
            if self.rowNum - 1 - self.l[-1] > d:
                res = self.rowNum-1
        bisect.insort(self.l, res)
        return res

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.l.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
