'''
Created on Apr 26, 2017

@author: MT
'''

class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        sumVal = sum(nums)
        if sumVal%4 != 0: return False
        target = sumVal//4
        # Faster
        nums.sort(reverse=True)
        return self.helper(nums, [0]*4, 0, target)
    
    def helper(self, nums, sums, ind, target):
        if ind == len(nums):
            if sums[0] == target and sums[1] == target and\
                sums[2] == target and sums[3] == target:
                return True
            return False
        for i in range(4):
            if sums[i]+nums[ind] > target:
                continue
            sums[i] += nums[ind]
            if self.helper(nums, sums, ind+1, target):
                return True
            sums[i] -= nums[ind]
        return False
    
    def test(self):
        testCases = [
            [1, 1, 2, 2, 2],
            [3, 3, 3, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.makesquare(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
