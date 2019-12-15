'''
Created on Mar 5, 2017

@author: MT
'''

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1: return k
        if n == 2: return k*k
        prev1 = k*k
        prev2 = k
        curr = 0
        for _ in range(2, n):
            curr = (prev1+prev2)*(k-1)
            prev2 = prev1
            prev1 = curr
        return curr
    
    def test(self):
        testCases = [
            (4, 3),
            (3, 2),
        ]
        for n, k in testCases:
            print('n: %s' % (n))
            print('k: %s' % (k))
            result = self.numWays(n, k)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

