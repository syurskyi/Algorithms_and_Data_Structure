'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return []
        sumArr = [0]
        usedColumns = [0]*n
        self.placeQueen(usedColumns, 0, sumArr)
        return sumArr[0]
    
    def placeQueen(self, usedColumns, row, sumArr):
        n = len(usedColumns)
        if row == n:
            sumArr[0] += 1
            return
        for i in range(n):
            if self.isValid(usedColumns, row, i):
                usedColumns[row] = i
                self.placeQueen(usedColumns, row+1, sumArr)
    
    def isValid(self, usedColumns, row, col):
        for i in range(row):
            if usedColumns[i] == col:
                return False
            if row-i == abs(col-usedColumns[i]):
                return False
        
        return True
    
    def test(self):
        for n in range(5):
            print('n: %s' % (n))
            result = self.totalNQueens(n)
            print('result: %s' % result)
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()