'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        stack = list(range(n-1, -1, -1))
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                res.insert(0, nums[stack[-1]])
            else:
                res.insert(0, -1)
            stack.append(i)
        return res
    
    def test(self):
        testCases = [
#             [1, 2, 1],
            [1, 6, 2, 7, 4, 5],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.nextGreaterElements(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
