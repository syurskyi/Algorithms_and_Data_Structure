'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n
        for num in nums:
            if 0 <= num-1 < n:
                dp[num-1] += 1
        for i, val in enumerate(dp):
            if val == 0:
                return i+1
        return len(nums)+1
