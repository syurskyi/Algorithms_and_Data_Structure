'''
Created on Aug 30, 2017

@author: MT
'''
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        maxLen = 0
        for num in nums:
            if num not in hashmap:
                hashset = set()
                count = 0
                num0 = num
                while num0 != num or count == 0:
                    count += 1
                    num0 = nums[num0]
                    hashset.add(num0)
                for num0 in hashset:
                    hashmap[num0] = count
                maxLen = max(maxLen, count)
        return maxLen
    
    def test(self):
        testCases = [
            [5,4,0,3,1,6,2],
            [0],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.arrayNesting(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
