'''
Created on Mar 7, 2017

@author: MT
'''

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j)
    
    def bfs(self, rooms, i, j):
        m, n = len(rooms), len(rooms[0])
        queue = [(i, j, 0)]
        while queue:
            i0, j0, dist = queue.pop(0)
            for x, y in ((i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1)):
                if 0 <= x < m and 0 <= y < n and rooms[x][y] != -1:
                    newDist = dist + 1
                    rooms[x][y] = min(rooms[x][y], newDist)
                    if rooms[x][y] > rooms[i0][j0]:
                        queue.append((x, y, newDist))
    
    def test(self):
        matrix = [
            [float('inf'), -1, 0, float('inf')],
            [float('inf'), float('inf'), float('inf'), -1],
            [float('inf'), -1, float('inf'), -1],
            [0, -1, float('inf'), float('inf')],
        ]
        print('before:')
        print('\n'.join([str(l) for l in matrix]))
        self.wallsAndGates(matrix)
        print('after:')
        print('\n'.join([str(l) for l in matrix]))
        print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
