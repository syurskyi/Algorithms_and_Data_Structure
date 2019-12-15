'''
Created on Jan 23, 2017

@author: MT
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        colors = [0]*3
        for num in nums:
            colors[num]+=1
        i, j = 0, 0
        while j < 3:
            if colors[j]:
                nums[i]=j
                colors[j] -= 1
                i += 1
            else:
                j += 1
    
    def test(self):
        testCases = [
            [2, 1, 0, 0, 1, 2, 2, 1],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            self.sortColors(nums)
            print('After sort')
            print('nums: %s' % (nums))
            print('-='*15+'-')
if __name__ == '__main__':
    Solution().test()
