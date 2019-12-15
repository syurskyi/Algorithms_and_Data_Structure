'''
Created on Aug 29, 2017

@author: MT
'''
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        matrix = M
        if not matrix or not matrix[0]: return 0
        maxLen = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[[0]*4 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                for k in range(4):
                    dp[i][j][k] = 1
                if j > 0:
                    dp[i][j][0] += dp[i][j-1][0]
                if j > 0 and i > 0:
                    dp[i][j][1] += dp[i-1][j-1][1]
                if i > 0:
                    dp[i][j][2] += dp[i-1][j][2]
                if i > 0 and j+1 < n:
                    dp[i][j][3] += dp[i-1][j+1][3]
                maxLen = max(maxLen, dp[i][j][0], dp[i][j][1],\
                             dp[i][j][2], dp[i][j][3])
        return maxLen
    
    def test(self):
        testCases = [
            [
                [0,1,1,0],
                [0,1,1,0],
                [0,0,0,1],
            ],
        ]
        for matrix in testCases:
            print('\n'.join([str(row) for row in matrix]))
            result = self.longestLine(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
