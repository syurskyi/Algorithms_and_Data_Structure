'''
Created on Oct 31, 2017

@author: MT
'''
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
    
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in '123456789':
                        if self.isValid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
    
    def isValid(self, board, row, col, c):
        for i in range(9):
            if board[i][col] == c: return False
            if board[row][i] == c: return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3] == c:
                return False
        return True
