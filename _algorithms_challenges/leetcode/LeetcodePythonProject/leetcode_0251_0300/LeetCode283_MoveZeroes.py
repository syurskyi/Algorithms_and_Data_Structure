'''
Created on Mar 6, 2017

@author: MT
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j+=1
        for i in range(j, len(nums)):
            nums[i] = 0
