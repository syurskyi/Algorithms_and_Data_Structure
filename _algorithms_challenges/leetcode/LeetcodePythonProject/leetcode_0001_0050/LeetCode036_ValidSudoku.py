'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            hashset = set()
            for j in range(9):
                if board[i][j] in hashset:
                    return False
                if board[i][j] != '.':
                    hashset.add(board[i][j])
        for j in range(9):
            hashset = set()
            for i in range(9):
                if board[i][j] in hashset:
                    return False
                if board[i][j] != '.':
                    hashset.add(board[i][j])
        for i0 in range(3):
            for j0 in range(3):
                hashset = set()
                for i in range(i0*3, i0*3+3):
                    for j in range(j0*3, j0*3+3):
                        if board[i][j] in hashset:
                            return False
                        if board[i][j] != '.':
                            hashset.add(board[i][j])
        return True
