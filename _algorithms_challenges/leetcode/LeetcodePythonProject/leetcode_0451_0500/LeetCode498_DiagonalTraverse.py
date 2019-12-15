'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]: return []
        if len(matrix) == 1: return matrix[0]
        if len(matrix[0]) == 1: return [row[0] for row in matrix]
        rev = False
        result = []
        m, n = len(matrix), len(matrix[0])
        for l in range(m+n-1):
            if rev:
                for i in range(l+1):
                    j = l-i
                    if 0 <= i < m and 0 <= j < n:
                        result.append(matrix[i][j])
            else:
                for j in range(l+1):
                    i = l-j
                    if 0 <= i < m and 0 <= j < n:
                        result.append(matrix[i][j])
            rev = not rev
        return result
