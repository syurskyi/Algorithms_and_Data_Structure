'''
Created on Oct 26, 2017

@author: MT
'''
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        hashmap = {}
        degree = 0
        cands = set()
        for i, num in enumerate(nums):
            hashmap[num] = hashmap.get(num, [])+[i]
            if len(hashmap[num]) > degree:
                degree = len(hashmap[num])
                cands = set([num])
            elif len(hashmap[num]) == degree:
                cands.add(num)
        minLen = float('inf')
        for num in cands:
            if len(hashmap[num]) == 1:
                return 1
            minLen = min(minLen, hashmap[num][-1]-hashmap[num][0]+1)
        return minLen
    
    def test(self):
        testCases = [
            [1, 2, 2, 3, 1],
            [1, 2, 2, 3, 1, 4, 2],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findShortestSubArray(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
