'''
Created on Oct 9, 2018

@author: tongq
'''
class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        n, k, w = N, K, W
        if k == 0 or n >= k+w: return 1
        dp = [1.0]+[0.0]*n
        wSum = 1.0
        for i in range(1, n+1):
            dp[i] = wSum/w
            if i < k: wSum += dp[i]
            if i - w >= 0: wSum -= dp[i-w]
        return sum(dp[k:])
    
    def test(self):
        testCases = [
            [10, 1, 10],
            [6, 1, 10],
            [21, 17, 10],
        ]
        for n, k, w in testCases:
            result = self.new21Game(n, k, w)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
