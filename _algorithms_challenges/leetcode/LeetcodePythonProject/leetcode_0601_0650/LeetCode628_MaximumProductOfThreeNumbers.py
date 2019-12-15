'''
Created on Sep 10, 2017

@author: MT
'''
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return 0
        s1, s2 = float('inf'), float('inf')
        l1, l2, l3 = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num < s1:
                s2 = s1
                s1 = num
            elif num < s2:
                s2 = num
            if num > l1:
                l3 = l2
                l2 = l1
                l1 = num
            elif num > l2:
                l3 = l2
                l2 = num
            elif num > l3:
                l3 = num
        res = float('-inf')
        for a1, a2, a3 in (l1, l2, l3), (s1, s2, l1):
            res = max(res, a1*a2*a3)
        return res
    
    def test(self):
        testCases = [
            [1,2,3],
            [1,2,3,4],
            [-1, -2, 0, 3],
            [-1, -2, -3, 1],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.maximumProduct(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
