'''
Created on Aug 28, 2017

@author: MT
'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = {0:1}
        sumVal = 0
        res = 0
        for num in nums:
            sumVal += num
            if sumVal-k in hashmap:
                res += hashmap[sumVal-k]
            hashmap[sumVal] = hashmap.get(sumVal, 0)+1
        return res
    
    def test(self):
        testCases = [
            [
                [1, 1, 1],
                2,
            ],
            [
                [1, 1, 1],
                3,
            ],
            [
                [1, 1, 1],
                1,
            ],
            [
                [1, 1, 1],
                0,
            ],
            [
                [1, -1, 1, -1, 2,-2],
                0,
            ],
        ]
        for nums, k in testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            res = self.subarraySum(nums, k)
            print('result: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
