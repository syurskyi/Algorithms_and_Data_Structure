'''
Created on Apr 5, 2017

@author: MT
'''

class Solution(object):
    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        count = 0
        res = -1
        for i, num in enumerate(self.nums):
            if target == num:
                if random.randint(0, count) == 0:
                    res = i
                count += 1
        return res
