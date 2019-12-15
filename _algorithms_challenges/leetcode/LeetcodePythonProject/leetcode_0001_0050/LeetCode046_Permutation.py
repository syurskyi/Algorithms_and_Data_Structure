'''
Created on Jan 19, 2017

@author: MT
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums: return res
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, curr, res):
        if nums == []:
            res.append(list(curr))
            return
        for i, num in enumerate(nums):
            curr.append(num)
            self.dfs(nums[:i]+nums[i+1:], curr, res)
            curr.pop()
    
    def test(self):
        testCases = [
            [1, 2, 3]
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.permute(nums)
            print('result: %s' % result)
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()