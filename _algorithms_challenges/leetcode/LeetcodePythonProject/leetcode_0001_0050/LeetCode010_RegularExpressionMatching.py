'''
Created on May 5, 2017

@author: MT
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(n):
            if p[j] == '*' and dp[0][j-1]:
                dp[0][j+1] = True
        for i in range(m):
            for j in range(n):
                if s[i] == p[j] or p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if p[j-1] == '.' or s[i] == p[j-1]:
                        dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j-1]
        return dp[-1][-1]
    
    def test(self):
        testCases = [
            ['aa', 'a'],
            ['aa', 'a*'],
            ['ab', '.*'],
            ['aab', 'c*a*b'],
            ['mississippi', 'mis*is*p*.'],
        ]
        for s, p in testCases:
            print('s: %s' % s)
            print('p: %s' % p)
            result = self.isMatch(s, p)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
