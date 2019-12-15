'''
Created on May 29, 2018

@author: tongq
'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = list(triangle[-1])
        n = len(triangle)
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(triangle[i][j]+dp[j], triangle[i][j]+dp[j+1])
        return dp[0]
