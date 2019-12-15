'''
Created on Mar 18, 2017

@author: MT
'''
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        first = [0]
        for num in nums:
            first.append(first[-1]+num)
        return self.mergeSort(0, len(first), first, lower, upper)
    
    def mergeSort(self, l, r, first, lower, upper):
        mid = (l+r)//2
        if mid == l:
            return 0
        count = self.mergeSort(l, mid, first, lower, upper)+\
            self.mergeSort(mid, r, first, lower, upper)
        i, j = mid, mid
        for left in first[l:mid]:
            while i < r and first[i]-left <  lower: i+=1
            while j < r and first[j]-left <= upper: j+=1
            count += j-i
        first[l:r] = sorted(first[l:r])
        return count
    
    def test(self):
        testCases = [
            (
                [-2,5,-1],
                [-2, 2],
            ),
            (
                [0, -3, -3, 1, 1, 2],
                [3, 5],
            ),
            (
                [2147483647,-2147483648,-1,0],
                [-1,0],
            ),
        ]
        for nums, (lower, upper) in testCases:
            print('nums: %s' % (nums))
            print('lower: %s' % (lower))
            print('upper: %s' % (upper))
            result = self.countRangeSum(nums, lower, upper)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
