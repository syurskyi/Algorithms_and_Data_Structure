'''
Created on Jun 5, 2018

@author: tongq
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p: return True
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[-1][-1] = True
        j = n-1
        while j >= 0 and p[j] == '*':
            dp[-1][j] = True
            j -= 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == p[j] or p[j] == '?':
                    dp[i][j] = dp[i+1][j+1]
                elif p[j] == '*':
                    dp[i][j] = dp[i][j+1] or dp[i+1][j]
        return dp[0][0]
