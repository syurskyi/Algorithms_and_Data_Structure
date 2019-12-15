'''
Created on May 6, 2017

@author: MT
'''

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for l in range(1, n):
            for i in range(n-l):
                j = i+l
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][n-1] >= 0
    
    def PredictTheWinner_DnC(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.mem = {}
        return self.helper(nums, 0, len(nums)-1) >= 0
    
    def helper(self, nums, start, end):
        n = len(nums)
        num = start*n+end
        if num in self.mem:
            return self.mem[num]
        if start == end:
            self.mem[num] = nums[start]
            return self.mem[num]
        res1 = nums[start]-self.helper(nums, start+1, end)
        res2 = nums[end]-self.helper(nums, start, end-1)
        result = max(res1, res2)
        self.mem[num] = result
        return result
    
    def test(self):
        testCases = [
            [1, 5, 2],
            [1, 5, 233, 7],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.PredictTheWinner_DnC(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
