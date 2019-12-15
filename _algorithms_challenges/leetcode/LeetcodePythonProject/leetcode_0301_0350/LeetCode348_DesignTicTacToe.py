'''
Created on Mar 21, 2017

@author: MT
'''
class TicTacToe(object):
    def __init__(self, n):
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagonal = 0
        self.antiDiagonal = 0
    
    def move(self, row, col, player):
        toAdd = 1 if player == 1 else -1
        self.rows[row] += toAdd
        self.cols[col] += toAdd
        if row == col:
            self.diagonal += toAdd
        if col == len(self.cols)-1-row:
            self.antiDiagonal += toAdd
        n = len(self.cols)
        if abs(self.rows[row]) == n or\
            abs(self.cols[col]) == n or\
            abs(self.diagonal) == n or\
            abs(self.antiDiagonal) == n:
            return player
        return 0
