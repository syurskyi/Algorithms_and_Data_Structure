'''
Created on Sep 5, 2017

@author: MT
'''
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0)+1
        maxLen = 0
        for num, count in hashmap.items():
            if num+1 in hashmap:
                maxLen = max(maxLen, count+hashmap[num+1])
        return maxLen
    
    def test(self):
        testCases = [
            [1,3,2,2,5,2,3,7],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findLHS(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
