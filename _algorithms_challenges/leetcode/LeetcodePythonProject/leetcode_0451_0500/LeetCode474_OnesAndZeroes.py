'''
Created on Apr 26, 2017

@author: MT
'''

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        l = len(strs)
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(l+1)]
        for i in range(l+1):
            nums = [0, 0]
            if i > 0:
                s = strs[i-1]
                count0 = s.count('0')
                count1 = len(s)-count0
                nums = [count0, count1]
            for j in range(m+1):
                for k in range(n+1):
                    if i == 0:
                        dp[i][j][k] = 0
                    elif j >= nums[0] and k >= nums[1]:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-nums[0]][k-nums[1]]+1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        return dp[l][m][n]
    
    def findMaxForm_slow(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # Knapsack Problem
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    count0 = s.count('0')
                    count1 = len(s)-count0
                    if i>=count0 and j>=count1:
                        dp[i][j] = max(dp[i][j], dp[i-count0][j-count1]+1)
        return dp[-1][-1]
    
    def test(self):
        testCases = [
            (
                ["10", "0001", "111001", "1", "0"], 5, 3
            ),
            (
                ["10", "0", "1"], 1, 1
            ),
        ]
        for strs, m, n in testCases:
            result = self.findMaxForm(strs, m, n)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
