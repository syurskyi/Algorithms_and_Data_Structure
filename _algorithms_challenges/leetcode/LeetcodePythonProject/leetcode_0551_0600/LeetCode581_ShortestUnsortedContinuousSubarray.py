'''
Created on Sep 4, 2017

@author: MT
'''
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSorted = sorted(nums)
        i, j = 0, len(nums)-1
        while i < j and numsSorted[i] == nums[i]:
            i += 1
        if i == j:
            return 0
        while i < j and numsSorted[j] == nums[j]:
            j -= 1
        return j-i+1
    
    def test(self):
        testCases = [
            [2, 6, 4, 8, 10, 9, 15],
            [1, 2, 3, 5],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findUnsortedSubarray(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
