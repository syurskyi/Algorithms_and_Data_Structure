'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0: return False
        w = t+1
        hashmap = {}
        for i, num in enumerate(nums):
            m = num//w
            if m in hashmap:
                return True
            if m+1 in hashmap and abs(hashmap[m+1]-num) < w:
                return True
            if m-1 in hashmap and abs(hashmap[m-1]-num) < w:
                return True
            hashmap[m] = num
            if i>=k:
                del hashmap[nums[i-k]//w]
        return False
