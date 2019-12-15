'''
Created on Nov 8, 2017

@author: MT
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        res = []
        for i, num in enumerate(nums):
            if target-num in hashmap:
                return [hashmap[target-num], i]
            hashmap[num] = i
        return res
