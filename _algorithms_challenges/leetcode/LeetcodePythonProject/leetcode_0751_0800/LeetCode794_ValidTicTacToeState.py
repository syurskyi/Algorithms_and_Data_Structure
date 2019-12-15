'''
Created on Apr 17, 2018

@author: tongq
'''
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        turns = 0
        rows = [0]*3
        cols = [0]*3
        diag = 0
        antidiag = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    turns += 1
                    rows[i] += 1
                    cols[j] += 1
                    if i == j: diag += 1
                    if i+j == 2: antidiag += 1
                elif board[i][j] == 'O':
                    turns -= 1
                    rows[i] -= 1
                    cols[j] -= 1
                    if i == j: diag -= 1
                    if i+j == 2: antidiag -= 1
        xwin = rows[0]==3 or rows[1]==3 or rows[2]==3 or\
            cols[0]==3 or cols[1]== 3 or cols[2]==3 or\
            diag == 3 or antidiag == 3
        owin = rows[0]==-3 or rows[1]==-3 or rows[2]==-3 or\
            cols[0]==-3 or cols[1]==-3 or cols[2]==-3 or\
            diag == -3 or antidiag == -3
        if (xwin and turns == 0) or (owin and turns == 1):
            return False
        return (turns==0 or turns==1) and (not xwin or not owin)
    
    def test(self):
        testCases = [
            ["O  ", "   ", "   "],
            ["XOX", " X ", "   "],
            ["XXX", "   ", "OOO"],
            ["XOX", "O O", "XOX"],
            ["XXX", "OOX", "OOX"],
            ["OXX", "XOX", "OXO"],
        ]
        for board in testCases:
            result = self.validTicTacToe(board)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()