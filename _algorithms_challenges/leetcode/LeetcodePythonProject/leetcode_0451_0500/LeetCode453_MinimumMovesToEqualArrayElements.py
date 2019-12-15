'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object):
    def minMoves(self, nums):
        res = 0
        minVal = min(nums)
        for num in nums:
            res += num - minVal
        return res
