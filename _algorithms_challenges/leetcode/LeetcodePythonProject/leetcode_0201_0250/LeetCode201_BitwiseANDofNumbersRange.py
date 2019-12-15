'''
Created on Feb 18, 2017

@author: MT
'''

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        moveFactor = 1
        while m != n:
            m >>= 1
            n >>= 1
            moveFactor <<= 1
        return moveFactor*m
    
    def test(self):
        testCases = [
            (5, 7),
            (5, 20),
            (3, 7),
            (101, 110),
        ]
        for m, n in testCases:
            print('m: %s, n: %s' % (m, n))
            result = self.rangeBitwiseAnd(m, n)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
    