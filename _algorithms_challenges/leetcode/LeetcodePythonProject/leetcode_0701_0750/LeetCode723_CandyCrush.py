'''
Created on Feb 20, 2018

@author: tongq
'''
class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(board), len(board[0])
        res = [[0]*n for _ in range(m)]
        while True:
            changed = False
            for i in range(m):
                for j in range(n):
                    changed = self.bfs(board, i, j) or changed
            if not changed:
                res = board
                break
            self.convert(res, board)
            board = res
        return res
    
    def bfs(self, board, i, j):
        if board[i][j] == 0: return False
        m, n = len(board), len(board[0])
        val = abs(board[i][j])
        changed = False
        if i+2 < m and val == abs(board[i+1][j]) == abs(board[i+2][j]):
            for i0 in range(i+1, m):
                if abs(board[i0][j]) == val:
                    board[i0][j] = -val
                else:
                    break
            changed = True
        if j+2 < n and val == abs(board[i][j+1]) == abs(board[i][j+2]):
            for j0 in range(j+1, n):
                if abs(board[i][j0]) == val:
                    board[i][j0] = -val
                else:
                    break
            changed = True
        if changed:
            board[i][j] = -val
        return changed
    
    def convert(self, res, board):
        m, n = len(res), len(res[0])
        for j in range(n):
            i0 = m-1
            for i in range(m-1, -1, -1):
                if board[i][j] > 0:
                    res[i0][j] = board[i][j]
                    i0 -= 1
            for i in range(i0, -1, -1):
                res[i][j] = 0
    
    def test(self):
        testCases = [
            [
                [110,5,112,113,114],
                [210,211,5,213,214],
                [310,311,3,313,314],
                [410,411,412,5,414],
                [5,1,512,3,3],
                [610,4,1,613,614],
                [710,1,2,713,714],
                [810,1,2,1,1],
                [1,1,2,2,2],
                [4,1,4,4,1014],
            ],
            [
                [4,5,5,4,5],[5,1,4,2,5],[4,3,1,2,2],[4,5,4,4,5],[3,3,1,1,3],
            ],
        ]
        for board in testCases:
            print('board:')
            print('\n'.join([str(row) for row in board]))
            result = self.candyCrush(board)
            print('result:')
            print('\n'.join([str(row) for row in result]))
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
