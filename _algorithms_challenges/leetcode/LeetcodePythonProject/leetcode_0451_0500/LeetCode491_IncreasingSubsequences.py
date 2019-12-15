'''
Created on May 8, 2017

@author: MT
'''

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        self.helper(nums, 0, [], res)
        return [list(row) for row in res]
    
    def helper(self, nums, ind, curr, res):
        if len(curr) >= 2:
            res.add(tuple(curr))
        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i-1]:
                continue
            if not curr or curr[-1] <= nums[i]:
                curr.append(nums[i])
                self.helper(nums, i+1, curr, res)
                curr.pop()
    
    def test(self):
        testCases = [
            [1, 1, 2, 3, 3],
            [4, 6, 7, 7],
            [4, 3, 2, 1],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findSubsequences(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
