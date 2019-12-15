'''
Created on Oct 9, 2017

@author: MT
'''
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(1, n):
            for j in range(n-i):
                dp[j][j+i] = i+1
                for k in range(j+1, j+i+1):
                    tmp = dp[j][k-1]+dp[k][j+i]
                    if s[k-1] == s[j+i]:
                        tmp -= 1
                    dp[j][j+i] = min(dp[j][j+i], tmp)
        return dp[0][n-1]
    
    def test(self):
        testCases = [
            'aaabbb',
            'aba',
            'abcabc',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.strangePrinter(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
