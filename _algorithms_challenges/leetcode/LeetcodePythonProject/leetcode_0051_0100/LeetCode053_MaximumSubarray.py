'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        maxVal = dp[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            maxVal = max(maxVal, dp[i])
        return maxVal
    
    def maxSubArrayDAC(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Divide and Co
        pass
    
    def test(self):
        testCases = [
            [-2,1,-3,4,-1,2,1,-5,4],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.maxSubArray(nums)
            print('result: %s' % (result))
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()