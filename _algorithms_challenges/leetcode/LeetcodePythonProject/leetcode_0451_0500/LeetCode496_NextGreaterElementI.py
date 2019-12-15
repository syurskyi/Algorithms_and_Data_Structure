'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for k, num0 in enumerate(findNums):
            ind = nums.index(num0)
            for i in range(ind, len(nums)):
                if nums[i] > num0:
                    res.append(nums[i])
                    break
            if len(res) == k:
                res.append(-1)
        return res
    
    def test(self):
        testCases = [
            (
                [4, 1, 2],
                [1, 3, 4, 2],
            ),
        ]
        for findNums, nums in testCases:
            result = self.nextGreaterElement(findNums, nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
