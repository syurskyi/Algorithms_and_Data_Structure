'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object):
    def find132pattern(self, nums):
        s3 = float('-inf')
        stack = []
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num < s3:
                return True
            while stack and stack[-1] < num:
                s3 = stack.pop()
            stack.append(num)
        return False
    
    def test(self):
        testCases = [
            [3, 1, 4, 2],
            [1, 2, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.find132pattern(nums)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
