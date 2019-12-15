'''
Created on Oct 19, 2017

@author: MT
'''
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}
        return self.helper(nums, hashmap)
    
    def helper(self, nums, hashmap):
        if len(nums) == 1:
            return abs(nums[0]-24) <= 0.0001
        nums = sorted(nums)
        if ''.join(str(nums) + ',') in hashmap:
            return False
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                a = nums[i]
                b = nums[j]
                nums1 = nums[:i]+nums[i+1:j]+nums[j+1:]
                if  self.helper(nums1 + [a+b], hashmap) or\
                    self.helper(nums1 + [a*b], hashmap) or\
                    self.helper(nums1 + [b-a], hashmap) or\
                    self.helper(nums1 + [a-b], hashmap) or\
                    (a != 0 and self.helper(nums1 + [float(b)/a], hashmap)) or\
                    (b != 0 and self.helper(nums1 + [float(a)/b], hashmap)):
                    return True
        hashmap[''.join(str(nums)+',')] = False
        return False
    
    def test(self):
        testCases = [
            [4, 1, 8, 7],
            [1, 2, 1, 2],
            [1, 5, 9, 1],
            [1, 8, 2, 5],
            [8, 1, 6, 6],
            [3, 3, 8, 8],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.judgePoint24(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
