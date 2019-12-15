'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object):
    def minPatches(self, nums, n):
        miss = 1
        added, i = 0, 0
        while miss <= n:
            if i < len(nums) and miss >= nums[i]:
                miss += nums[i]
                i+=1
            else:
                miss += miss
                added += 1
        return added
