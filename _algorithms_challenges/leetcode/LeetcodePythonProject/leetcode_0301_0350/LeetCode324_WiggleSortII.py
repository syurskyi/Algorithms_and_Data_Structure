
class Solution(object):
    def wiggleSort(self, nums):
        median = self.kthLargestElement(nums, (len(nums)+1)//2)
        n = len(nums)
        left = 0
        i = 0
        right = n-1
        while i <= right:
            if nums[self.newIndex(i, n)] > median:
                nums[self.newIndex(left, n)], nums[self.newIndex(i, n)] =\
                nums[self.newIndex(i, n)], nums[self.newIndex(left, n)]
                left += 1
                i += 1
            elif nums[self.newIndex(i, n)] < median:
                nums[self.newIndex(right, n)], nums[self.newIndex(i, n)] =\
                nums[self.newIndex(i, n)], nums[self.newIndex(right, n)]
                right -= 1
            else:
                i += 1
    
    def newIndex(self, index, n):
        return (1+2*index)%(n|1)
    
    def kthLargestElement(self, nums, k):
        self.shuffle(nums)
        lo = 0
        hi = len(nums)-1
        k = len(nums)-k
        while lo < hi:
            j = self.partition(nums, lo, hi)
            if j < k:
                lo = j+1
            elif j > k:
                hi = j-1
            else:
                break
        return nums[k]
    
    def partition(self, nums, lo, hi):
        i, j = lo+1, hi
        while True:
            while i < hi and nums[i] <= nums[lo]:
                i += 1
            while j > lo and nums[lo] <= nums[j]:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[lo], nums[j] = nums[j], nums[lo]
        return j
    
    def shuffle(self, nums):
        import random
        for i in range(len(nums)-1, 0, -1):
            ind = random.randint(0, i)
            nums[i], nums[ind] = nums[ind], nums[i]
    
    def wiggleSortWithSorting(self, nums):
        nums.sort()
        half = len(nums[::2])-1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
    
    def test(self):
        testCases = [
            [1, 5, 1, 1, 6, 4],
            [1, 3, 2, 2, 3, 1],
            [1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            self.wiggleSort(nums)
            print('sorted: %s' % (nums))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
