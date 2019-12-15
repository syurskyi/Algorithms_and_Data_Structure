class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        newboard = []
        for i in range(n):
            newboard.extend(board[n-i-1] if i % 2 == 0 else board[n-i-1][::-1])
        board = newboard
        n = len(board)
        queue = [(0, 0)]
        visited = set([0])
        while queue:
            i, d = queue.pop(0)
            for j in range(i+1, i+7):
                if j == n-1:
                    return d+1
                if j not in visited:
                    visited.add(j)
                    if board[j] == -1:
                        queue.append((j, d+1))
                    else:
                        if board[j] == n:
                            return d+1
                        if board[board[j]-1] == -1:
                            visited.add(board[j]-1)
                            # if not, later moves can visit it again?
                        queue.append((board[j]-1, d+1))
        return -1

    def test(self):
        testCases = [
            [[-1, 1, 2,-1],
             [2, 13,15,-1],
             [-1,10,-1,-1],
             [-1, 6, 2,8]],

            [[-1,7,-1],
             [-1,6,9],
             [-1,-1,2]],

            [[-1,-1,-1],
             [-1,9,8],
             [-1,8,9]],

            [[-1,4,-1],
             [6,2,6],
             [-1,3,-1]],

            [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1]],

            [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1]],
        ]
        for board in testCases:
            res = self.snakesAndLadders(board)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
