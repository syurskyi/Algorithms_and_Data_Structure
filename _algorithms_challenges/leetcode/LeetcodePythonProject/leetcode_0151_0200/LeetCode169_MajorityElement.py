'''
Created on Feb 13, 2017

@author: MT
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, cand = 0, -1
        for num in nums:
            if cand == num:
                count += 1
            elif count == 0:
                cand, count = num, 1
            else:
                count -= 1
        return cand
    
    def test(self):
        testCases = [
            [1, 2, 2, 3, 2],
            [5, 1, 1, 1, 3],
            [1, 1, 1, 3],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.majorityElement(nums)
            print('result: %s' % (result))
            print('-='*20 + '-')

if __name__ == '__main__':
    Solution().test()