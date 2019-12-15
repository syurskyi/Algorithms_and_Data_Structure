'''
Created on Jan 24, 2017

@author: MT
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        elem = []
        self.helper(nums, elem, 0, result)
        return result
    
    def helper(self, nums, elem, start, result):
        result.append(list(elem))
        for i in range(start, len(nums)):
            elem.append(nums[i])
            self.helper(nums, elem, i+1, result)
            elem.pop()
    
    def test(self):
        testCases = [
            [1, 2, 3],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.subsets(nums)
            print('result: %s' % (result))
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()
