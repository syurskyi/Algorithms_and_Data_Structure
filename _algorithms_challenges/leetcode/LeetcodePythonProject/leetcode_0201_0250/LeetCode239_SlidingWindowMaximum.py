'''
Created on Feb 26, 2017

@author: MT
'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        deque = []
        for i, num in enumerate(nums):
            if deque and deque[0] == i-k:
                deque.pop(0)
            while deque and nums[deque[-1]] < num:
                deque.pop()
            deque.append(i)
            if i+1>=k:
                res.append(nums[deque[0]])
        return res
    
    def test(self):
        testCases = [
            ([1,3,-1,-3,5,3,6,7], 3),
        ]
        for nums, k in testCases:
            print('nums: %s' % (nums))
            result = self.maxSlidingWindow(nums, k)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
