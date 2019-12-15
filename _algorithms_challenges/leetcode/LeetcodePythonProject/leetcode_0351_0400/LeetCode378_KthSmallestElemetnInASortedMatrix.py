'''
Created on Apr 1, 2017

@author: MT
'''

class Solution(object):
    def kthSmallest(self, matrix, k):
        lower, upper = matrix[0][0], matrix[-1][-1]
        while lower < upper:
            mid = (lower+upper)//2
            if self.count(matrix, mid) < k:
                lower = mid+1
            else:
                upper = mid
        return upper
    
    def count(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        count = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= target:
                count += i+1
                j += 1
            else:
                i -= 1
        return count
    
    def test(self):
        matrix = [
            [ 1,  5,  9],
            [10, 11, 13],
            [12, 13, 15],
        ]
        nums = [1, 5, 9, 10, 13]
        for num in nums:
            print('num: %s' % num)
            print('count: %s' % self.count(matrix, num))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
