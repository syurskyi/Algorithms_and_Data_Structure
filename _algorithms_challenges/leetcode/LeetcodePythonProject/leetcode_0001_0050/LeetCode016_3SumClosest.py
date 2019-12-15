'''
Created on Nov 7, 2017

@author: MT
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = float('inf')
        n = len(nums)
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                tmp = nums[i]+nums[j]+nums[k]
                diff = abs(tmp-target)
                if diff < abs(res-target):
                    res = tmp
                if tmp == target:
                    return target
                elif tmp > target:
                    k -= 1
                else:
                    j += 1
        return res
    
    def test(self):
        testCases = [
            [
                [-1, 2, 1, -4],
                1,
            ],
        ]
        for nums, target in testCases:
            print('nums: %s' % nums)
            print('target: %s' % target)
            result = self.threeSumClosest(nums, target)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
