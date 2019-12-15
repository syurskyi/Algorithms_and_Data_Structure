'''
Created on Jan 28, 2017

@author: MT
'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, n+1):
            first = int(s[i-1])
            second = int(s[i-2:i])
            if 1 <= first <= 9:
                dp[i] += dp[i-1]
            if 10 <= second <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
    
    def numDecodings_orig(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0]*(len(s))
        dp[0] = 1
        if int(s[0:2]) > 26:
            if s[1] != '0':
                dp[1] = 1
            else:
                dp[1] = 0
        else:
            if s[1] != '0':
                dp[1] = 2
            else:
                dp[1] = 1
        n = len(s)
        
        for i in range(2, n):
            if s[i] != '0':
                dp[i] += dp[i-1]
            val = int(s[i-1:i+1])
            if val<=26 and val>=10:
                dp[i] += dp[i-2]
        
        return dp[-1]
    
    def test(self):
        testCases = [
            '111',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.numDecodings(s)
            print('result: %s' % (result))
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()