'''
Created on Feb 22, 2017

@author: MT
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if not nums: return result
        i = 0
        while i < len(nums):
            start = nums[i]
            while i+1 < len(nums) and nums[i+1] == nums[i]+1:
                i+=1
            end = nums[i]
            if end == start:
                result.append('%s' % (start))
            else:
                result.append('%s->%s' % (start, end))
            i += 1
        return result