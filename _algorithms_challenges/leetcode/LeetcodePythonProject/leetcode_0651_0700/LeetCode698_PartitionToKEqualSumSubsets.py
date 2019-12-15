'''
Created on Oct 26, 2017

@author: MT
'''
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sumVal = sum(nums)
        if sumVal%k != 0:
            return False
        nums.sort(reverse=True)
        return self.helper(nums, [0]*k, sumVal//k, 0, k)
    
    def helper(self, nums, elems, target, ind, k):
        if ind == k:
            return True
        for i in range(len(nums)):
            if elems[ind]+nums[i] <= target:
                elems[ind] += nums[i]
                if elems[ind] == target and\
                    self.helper(nums[:i]+nums[i+1:], elems, target, ind+1, k):
                    return True
                elif self.helper(nums[:i]+nums[i+1:], elems, target, ind, k):
                    return True
                elems[ind] -= nums[i]
            else:
                break
        return False
    
    def test(self):
        testCases = [
            [
                [4, 3, 2, 3, 5, 2, 1],
                4,
            ],
            [
                [730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908],
                4,
            ],
            [
                [4,5,3,2,5,5,5,1,5,5,5,5,3,5,5,2],
                13,
            ],
        ]
        for nums, k in testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = self.canPartitionKSubsets(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
