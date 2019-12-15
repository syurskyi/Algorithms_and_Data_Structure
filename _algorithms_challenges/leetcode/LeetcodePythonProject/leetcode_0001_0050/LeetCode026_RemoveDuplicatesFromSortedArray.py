'''
Created on Nov 2, 2017

@author: MT
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i, num in enumerate(nums):
            if i == 0 or nums[i-1] != num:
                nums[j] = num
                j += 1
        return j
