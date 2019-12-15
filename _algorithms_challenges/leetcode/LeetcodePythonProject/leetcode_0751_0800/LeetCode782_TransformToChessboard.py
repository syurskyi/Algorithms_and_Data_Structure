'''
Created on Apr 9, 2018

@author: tongq
'''
class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        rowSum, colSum, rowSwap, colSwap = 0, 0, 0, 0
        for i in range(n):
            for j in range(n):
                if board[0][0]^board[i][0]^board[0][j]^board[i][j] == 1:
                    return -1
        for i in range(n):
            rowSum += board[0][i]
            colSum += board[i][0]
            if board[i][0] == i%2:
                rowSwap += 1
            if board[0][i] == i%2:
                colSwap += 1
        if n//2 > rowSum or rowSum > (n+1)//2:
            return -1
        if n//2 > colSum or colSum > (n+1)//2:
            return -1
        if n % 2 == 1:
            if colSwap%2 == 1:
                colSwap = n-colSwap
            if rowSwap%2 == 1:
                rowSwap = n-rowSwap
        else:
            colSwap = min(n-colSwap, colSwap)
            rowSwap = min(n-rowSwap, rowSwap)
        return (colSwap+rowSwap)//2
    
    def test(self):
        testCases = [
            [
                [0,1,1,0],
                [0,1,1,0],
                [1,0,0,1],
                [1,0,0,1],
            ],
            [
                [0, 1],
                [1, 0],
            ],
            [
                [1, 0],
                [1, 0],
            ],
        ]
        for board in testCases:
            result = self.movesToChessboard(board)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
