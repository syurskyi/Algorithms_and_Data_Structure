'''
Created on Sep 6, 2017

@author: MT
'''
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(len(nums)-1, 0, -1):
            l, r = 0, i-1
            while l < r:
                if nums[l]+nums[r] > nums[i]:
                    count += r-l
                    r -= 1
                else:
                    l += 1
        return count
    
    def test(self):
        testCases = [
            [2, 2, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.triangleNumber(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
