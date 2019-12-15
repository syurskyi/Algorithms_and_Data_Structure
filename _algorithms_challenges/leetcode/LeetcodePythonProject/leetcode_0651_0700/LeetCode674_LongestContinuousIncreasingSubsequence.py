'''
Created on Oct 15, 2017

@author: MT
'''
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        i = 0
        res = 1
        while i < n:
            j = i
            while i+1 < n and nums[i] < nums[i+1]:
                i += 1
                res = max(res, i-j+1)
            i += 1
        return res
    
    def test(self):
        testCases = [
            [1, 3, 5, 4, 7],
            [2, 2, 2, 2, 2],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findLengthOfLCIS(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
