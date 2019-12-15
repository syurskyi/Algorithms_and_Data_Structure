'''
Created on Oct 3, 2017

@author: MT
'''
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        for i in range(2, n+1):
            dp[i] = i
            for j in range(i-1, -1, -1):
                if i%j == 0:
                    dp[i] = dp[j]+i//j
                    break
        return dp[-1]
    
    def test(self):
        testCases = [
            1,
            2,
            3,
            4,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.minSteps(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
