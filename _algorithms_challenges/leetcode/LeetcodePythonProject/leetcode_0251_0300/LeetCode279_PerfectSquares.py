'''
Created on Mar 5, 2017

@author: MT
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        maxVal = int(math.sqrt(n))+1
        if n < 0: return 0
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(n+1):
            for j in range(maxVal):
                if j*j<=i:
                    dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]
    
    def test(self):
        testCases = [
            12,
            13,
            24,
        ]
        for n in testCases:
            print('n: %s' % (n))
            result = self.numSquares(n)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
