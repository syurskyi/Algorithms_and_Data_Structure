'''
Created on Apr 5, 2018

@author: tongq
'''
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        s = ''.join([str(n) for n in board[0]])+''.join([str(n) for n in board[1]])
        visited = set([s])
        target = '123450'
        queue = [s]
        res = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                s = queue.pop(0)
                if s == target:
                    return res
                i = s.index('0')
                for j in [i+1, i-1, i+3, i-3]:
                    if j < 0 or j > 5 or\
                        (i == 2 and j == 3) or\
                        (i == 3 and j == 2):
                        continue
                    arr = list(s)
                    arr[i], arr[j] = arr[j], arr[i]
                    newS = ''.join(arr)
                    if newS not in visited:
                        visited.add(newS)
                        queue.append(newS)
            res += 1
        return -1
    
    def getZero(self, board):
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    return i, j
    
    def test(self):
        testCases = [
            [[1,2,3],[4,0,5]],
            [[1,2,3],[5,4,0]],
            [[4,1,2],[5,0,3]],
            [[3,2,4],[1,5,0]],
        ]
        for board in testCases:
            print('board')
            print('\n'.join([str(row) for row in board]))
            result = self.slidingPuzzle(board)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
