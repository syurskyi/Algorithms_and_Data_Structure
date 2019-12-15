'''
Created on Feb 26, 2017

@author: MT
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
    
    def searchMatrix_orig(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
    
    def searchMatrixBinary(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        start, end = 0, len(matrix)-1
        while start <= end:
            mid = int((start+end)/2)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid-1
            else:
                start = mid+1
        row0 = start if start < len(matrix) else start-1
        for row in range(row0, -1, -1):
            start, end = 0, len(matrix[0])-1
            while start <= end:
                mid = int((start+end)/2)
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    end = mid-1 
                else:
                    start = mid+1
        return False
    
    def test(self):
        testCases = [
            [
                [1,   4,  7, 11, 15],
                [2,   5,  8, 12, 19],
                [3,   6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
        ]
        for matrix in testCases:
            for target in (0, 1, 3, 5, 13, 16, 20):
                print('target: %s' % target)
                result = self.searchMatrix(matrix, target)
                print('result: %s' % (result))
                print('-='*20+'-')
    
if __name__ == '__main__':
    Solution().test()
