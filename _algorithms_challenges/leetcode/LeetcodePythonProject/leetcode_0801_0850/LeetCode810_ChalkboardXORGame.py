'''
Created on Apr 25, 2018

@author: tongq
'''
class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from functools import reduce
        from operator import xor
        return len(nums)%2==0 or reduce(xor,nums)==0
    
    def xorGame_own_TLE(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = {}
        return self.helper(nums, mem)
    
    def helper(self, nums, mem):
        s = str(nums)
        if s in mem:
            return mem[s]
        if self.calc(nums) == 0:
            mem[s] = True
            return True
        flag = False
        for i in range(len(nums)):
            if not self.helper(nums[:i]+nums[i+1:], mem):
                flag = True
                break
        mem[s] = flag
        return flag
    
    def calc(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
    
    def test(self):
        testCases = [
#             [1, 1, 2],
            [1, 1, 2, 3], # True
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.xorGame(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
