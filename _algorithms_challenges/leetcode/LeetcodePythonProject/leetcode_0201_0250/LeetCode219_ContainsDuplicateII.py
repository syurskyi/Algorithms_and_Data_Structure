'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        for i, num in enumerate(nums):
            if num not in hashmap or i - hashmap[num] > k:
                hashmap[num] = i
            else:
                return True
        return False
    