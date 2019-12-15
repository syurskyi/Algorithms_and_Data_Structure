'''
Created on Oct 3, 2017

@author: MT
'''
class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] = max(dp[i], i)
            for j in range(1, n+1):
                if i+j+2 < n+1:
                    dp[i+j+2] = max(dp[i+j+2], dp[i]*(j+1))
        return dp[-1]
    
    def test(self):
        testCases = [
            1,
            2,
            3,
            7,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.maxA(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
