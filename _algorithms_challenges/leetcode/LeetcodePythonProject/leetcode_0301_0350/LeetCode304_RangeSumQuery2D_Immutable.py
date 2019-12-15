'''
Created on Mar 11, 2017

@author: MT
'''

class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix:
            self.tbl = None
            return
        m, n = len(matrix), len(matrix[0])
        tbl = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                tbl[i+1][j+1] = tbl[i][j+1]+tbl[i+1][j]+matrix[i][j]-tbl[i][j]
        self.tbl = tbl
    
    def sumRegion(self, row1, col1, row2, col2):
        return self.tbl[row2+1][col2+1] -\
            self.tbl[row2+1][col1] -\
            self.tbl[row1][col2+1]+\
            self.tbl[row1][col1]

if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    numMatrix = NumMatrix(matrix)
    print(numMatrix.sumRegion(2, 1, 4, 3))
    print(numMatrix.sumRegion(1, 1, 2, 2))
    print(numMatrix.sumRegion(1, 2, 2, 4))
    print('-='*30+'-')
