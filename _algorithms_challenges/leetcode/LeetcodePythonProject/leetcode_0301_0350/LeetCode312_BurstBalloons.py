'''
Created on Mar 15, 2017

@author: MT
'''

class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for k in range(2, n):
            for left in range(n-k):
                right = left + k
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right],\
                        nums[left]*nums[i]*nums[right]+\
                        dp[left][i]+\
                        dp[i][right])
        return dp[0][-1]
    
    def maxCoinsDnC(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        memo = [[0]*n for _ in range(n)]
        return self.burst(memo, nums, 0, n-1)
    
    def burst(self, memo, nums, left, right):
        if left+1 == right: return 0
        if memo[left][right] > 0:
            return memo[left][right]
        result = 0
        for i in range(left+1, right):
            result = max(result,\
                nums[left]*nums[i]*nums[right] + \
                self.burst(memo, nums, left, i) +\
                self.burst(memo, nums, i, right))
            memo[left][right] = result
        return result
    
    def test(self):
        testCases = [
            [3, 1, 5, 8],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.maxCoins(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
