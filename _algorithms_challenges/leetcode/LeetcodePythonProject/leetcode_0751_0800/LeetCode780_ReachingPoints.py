'''
Created on Apr 8, 2018

@author: tongq
'''
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while sx < tx and sy < ty:
            tx, ty = tx%ty, ty%tx
        if sx == tx and (ty-sy) % sx == 0 or\
            sy == ty and (tx-sx) % sy == 0:
            return True
        else:
            return False
    
    # RuntimeError: maximum recursion depth exceeded
    def reachingPoints_own(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        mem = {}
        return self.helper(sx, sy, tx, ty, mem)
    
    def helper(self, sx, sy, tx, ty, mem):
        if sx == tx and sy == ty:
            mem[(sx, sy)] = True
            return True
        if sx > tx or sy > ty:
            mem[(sx, sy)] = False
            return False
        if (sx, sy) in mem:
            return mem[(sx, sy)]
        res = self.helper(sx, sx+sy, tx, ty, mem) or\
            self.helper(sx+sy, sy, tx, ty, mem)
        mem[(sx, sy)] = res
        return res
    
    def test(self):
        testCases = [
            [1, 1, 3, 5], # True
            [1, 1, 2, 2], # False
            [1, 1, 1, 1], # True
            [6, 5, 11, 16], # True
        ]
        for sx, sy, tx, ty in testCases:
            print('sx: %s, sy: %s, tx: %s, ty: %s' % (sx, sy, tx, ty))
            result = self.reachingPoints(sx, sy, tx, ty)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
