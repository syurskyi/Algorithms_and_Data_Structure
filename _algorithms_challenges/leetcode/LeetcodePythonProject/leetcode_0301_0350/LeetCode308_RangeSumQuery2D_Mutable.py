'''
Created on Mar 13, 2017

@author: MT
'''
class NumMatrix_BinaryIndexTree_TLE(object):
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.m, self.n = m, n
        if not m or not n: return
        self.tree = [[0]*(n+1) for _ in range(m+1)]
        self.nums = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])
    
    def update(self, row, col, val):
        m, n = self.m, self.n
        if not m or not n: return
        delta = val-self.nums[row][col]
        self.nums[row][col] = val
        i = 0
        while i < m+1:
            j = 0
            while j < n+1:
                self.tree[i][j] += delta
                j += j&(-1)
            i += i&(-i)
    
    def sumRegion(self, row1, col1, row2, col2):
        m, n = self.m, self.n
        if not m or not n:
            return 0
        return self.sumHelper(row2+1, col2+1)\
                +self.sumHelper(row1, col1)\
                -self.sumHelper(row1, col2+1)\
                -self.sumHelper(row2+1, col1)
        
    def sumHelper(self, row, col):
        sumVal = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                sumVal += self.tree[i][j]
                j -= j&(-j)
            i -= i&(-i)
        return sumVal

class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix:
            return
        self.matrix = matrix
        m, n = len(matrix), len(matrix[0])
        colSums = [[0]*n for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n):
                colSums[i][j] = colSums[i-1][j] + matrix[i-1][j]
        self.colSums = colSums
    
    def update(self, row, col, val):
        for i in range(row+1, len(self.colSums)):
            self.colSums[i][col] = self.colSums[i][col]+val-self.matrix[row][col]
        self.matrix[row][col] = val
    
    def sumRegion(self, row1, col1, row2, col2):
        result = 0
        for j in range(col1, col2+1):
            result += self.colSums[row2+1][j] - self.colSums[row1][j]
        return result