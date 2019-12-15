'''
Created on May 11, 2017

@author: MT
'''

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        sortNums = sorted(nums, reverse=True)
        hashmap = {}
        for i, num in enumerate(sortNums):
            hashmap[num] = i+1
        for num in nums:
            ind = hashmap[num]
            if ind == 1:
                result.append('Gold Medal')
            elif ind == 2:
                result.append('Silver Medal')
            elif ind == 3:
                result.append('Bronze Medal')
            else:
                result.append(str(ind))
        return result
