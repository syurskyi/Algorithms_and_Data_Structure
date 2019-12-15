'''
Created on Apr 18, 2017

@author: MT
'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            ind = abs(num)-1
            if nums[ind] > 0:
                nums[ind] = -nums[ind]
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        return res
