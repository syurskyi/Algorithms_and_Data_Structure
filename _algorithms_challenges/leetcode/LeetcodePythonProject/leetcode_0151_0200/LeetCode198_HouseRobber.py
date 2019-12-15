'''
Created on Feb 16, 2017

@author: MT
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        include, exclude = 0, 0
        for num in nums:
            i, e = include, exclude
            include = e+num
            exclude = max(i, e)
        return max(include, exclude)
