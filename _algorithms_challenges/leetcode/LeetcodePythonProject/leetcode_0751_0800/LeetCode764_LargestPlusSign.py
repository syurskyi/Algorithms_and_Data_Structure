'''
Created on Apr 2, 2018

@author: tongq
'''
class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        n = N
        matrix = [[1]*n for _ in range(n)]
        for i, j in mines:
            matrix[i][j] = 0
        maxLen = 0
        dp = [[[0]*4 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                if i == 0 and j == 0:
                    dp[i][j][0] = 1
                    dp[i][j][1] = 1
                elif i == 0 and j != 0:
                    dp[i][j][0] = dp[i][j-1][0]+1
                    dp[i][j][1] = 1
                elif i != 0 and j == 0:
                    dp[i][j][0] = 1
                    dp[i][j][1] = dp[i-1][j][1]+1
                else:
                    dp[i][j][0] = dp[i][j-1][0]+1
                    dp[i][j][1] = dp[i-1][j][1]+1
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 0:
                    continue
                if i == n-1 and j == n-1:
                    dp[i][j][2] = 1
                    dp[i][j][3] = 1
                elif i == n-1 and j != n-1:
                    dp[i][j][2] = 1
                    dp[i][j][3] = dp[i][j+1][3]+1
                elif i != n-1 and j == n-1:
                    dp[i][j][2] = dp[i+1][j][2]+1
                    dp[i][j][3] = 1
                else:
                    dp[i][j][2] = dp[i+1][j][2]+1
                    dp[i][j][3] = dp[i][j+1][3]+1
        for i in range(n):
            for j in range(n):
                maxLen = max(maxLen, min(dp[i][j]))
        return maxLen
    
    def test(self):
        testCases = [
            [5, [[4, 2]]],
            [2, []],
            [1, [[0, 0]]],
            [2, [[0, 0], [1,1]]],
            [5, [[3,0],[3,3]]],
            [5, [[0,1],[0,2],[1,0],[1,2],[1,4],[2,0],[2,2],[3,0],[3,1],[4,0],[4,1],[4,3],[4,4]]],
        ]
        for n, mines in testCases:
            print('n: %s' % n)
            print('mines: %s' % mines)
            result = self.orderOfLargestPlusSign(n, mines)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
