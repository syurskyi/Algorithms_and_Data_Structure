'''
Created on Oct 10, 2017

@author: MT
'''
class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        hashmap = {}
        for num in nums:
            key = num//10
            value = num%10
            hashmap[key] = value
        self.sumVal = 0
        self.traverse(nums[0]//10, 0, hashmap)
        return self.sumVal
    
    def traverse(self, root, preSum, hashmap):
        level = root//10
        pos = root%10
        left = (level+1)*10+pos*2-1
        right = (level+1)*10+pos*2
        curSum = preSum + hashmap[root]
        if left not in hashmap and right not in hashmap:
            self.sumVal += curSum
            return
        if left in hashmap:
            self.traverse(left, curSum, hashmap)
        if right in hashmap:
            self.traverse(right, curSum, hashmap)
    
    def test(self):
        testCases = [
            [113, 215, 221],
            [113, 221],
            [111,217,221,315,415],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.pathSum(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
