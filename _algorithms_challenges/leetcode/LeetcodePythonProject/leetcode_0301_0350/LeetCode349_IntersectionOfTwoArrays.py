'''
Created on Mar 21, 2017

@author: MT
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        result = []
        for c1 in s1:
            if c1 in s2:
                result.append(c1)
        return result
