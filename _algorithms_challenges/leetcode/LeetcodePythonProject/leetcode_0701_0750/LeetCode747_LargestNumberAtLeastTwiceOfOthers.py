'''
Created on Mar 24, 2018

@author: tongq
'''
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        first, fInd = float('-inf'), -1
        second = float('-inf')
        for i, num in enumerate(nums):
            if num > first:
                second = first
                first = num
                fInd = i
            elif num > second:
                second = num
        return fInd if first >= 2*second else -1
    
    def test(self):
        testCases = [
            [3, 6, 1, 0],
            [1, 2, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.dominantIndex(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
