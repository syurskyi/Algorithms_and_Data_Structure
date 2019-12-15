'''
Created on Mar 4, 2017

@author: MT
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        length = len(nums)
        sumVal = (length+1)*(length)/2
        result = sumVal
        for num in nums:
            result -= num
        return result
    
    