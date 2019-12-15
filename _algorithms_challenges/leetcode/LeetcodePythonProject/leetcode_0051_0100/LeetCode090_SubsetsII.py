'''
Created on May 31, 2018

@author: tongq
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.helper(nums, 0, [], res)
        return res
    
    def helper(self, nums, ind, curr, res):
        res.append(list(curr))
        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i-1]:
                continue
            curr.append(nums[i])
            self.helper(nums, i+1, curr, res)
            curr.pop()
