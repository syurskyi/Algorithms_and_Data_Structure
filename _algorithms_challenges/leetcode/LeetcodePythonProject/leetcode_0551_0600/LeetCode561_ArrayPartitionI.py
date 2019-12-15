'''
Created on Aug 28, 2017

@author: MT
'''

class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])
