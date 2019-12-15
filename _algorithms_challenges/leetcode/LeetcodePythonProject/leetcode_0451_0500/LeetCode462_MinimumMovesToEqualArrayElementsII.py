'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object):
    def minMoves2(self, nums):
        if not nums: return 0
        nums.sort()
        left, right = 0, len(nums)-1
        count = 0
        while left < right:
            count += nums[right]-nums[left]
            left += 1
            right -= 1
        return count
