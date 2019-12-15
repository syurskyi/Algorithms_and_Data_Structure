'''
Created on Nov 7, 2017

@author: MT
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k, l = j+1, n-1
                while k < l:
                    tmp = nums[i]+nums[j]+nums[k]+nums[l]
                    if tmp == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k-1] == nums[k]:
                            k += 1
                        while k < l and nums[l+1] == nums[l]:
                            l -= 1
                    elif tmp < target:
                        k += 1
                    else:
                        l -= 1
        return res
    
    def test(self):
        testCases = [
            [
                [1,0,-1,0,-2,2],
                0,
            ],
        ]
        for nums, target in testCases:
            print('nums: %s' % nums)
            result = self.fourSum(nums, target)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
