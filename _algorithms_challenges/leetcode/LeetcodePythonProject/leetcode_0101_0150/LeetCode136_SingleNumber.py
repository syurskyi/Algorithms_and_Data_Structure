'''
Created on May 24, 2018

@author: tongq
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums: res ^= num
        return res
