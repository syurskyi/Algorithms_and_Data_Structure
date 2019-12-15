'''
Created on Nov 2, 2017

@author: MT
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for num in nums:
            if num != val:
                nums[j] = num
                j += 1
        return j
