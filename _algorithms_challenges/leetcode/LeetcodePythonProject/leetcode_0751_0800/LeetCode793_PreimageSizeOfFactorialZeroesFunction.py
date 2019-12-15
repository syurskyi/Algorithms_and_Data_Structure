'''
Created on Apr 17, 2018

@author: tongq
'''
class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        dp = [0]*13
        dp[0] = 1
        for i in range(1, 13):
            dp[i] = dp[i-1]*5+1
        for i in range(12, -1, -1):
            if K//dp[i] == 5:
                return 0
            K = K%dp[i]
        return 5
    
    def test(self):
        testCases = [
            0,
            5,
        ]
        for k in testCases:
            print('k: %s' % k)
            result = self.preimageSizeFZF(k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
