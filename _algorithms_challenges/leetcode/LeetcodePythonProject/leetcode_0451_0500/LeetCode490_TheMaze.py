'''
Created on May 8, 2017

@author: MT
'''

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n = len(maze), len(maze[0])
        queue= [start]
        visited = [[False]*n for _ in range(m)]
        visited[start[0]][start[1]] = True
        while queue:
            i, j = queue.pop(0)
            if i == destination[0] and j == destination[1]:
                return True
            visited[i][j] = True
            for x, y in self.getNextSteps(maze, i, j):
                if not visited[x][y]:
                    queue.append((x, y))
        return False
    
    def getNextSteps(self, maze, i, j):
        result = set()
        dirs = (1, 0), (0, 1), (-1, 0), (0, -1)
        m, n = len(maze), len(maze[0])
        for dir in dirs:
            x, y = i, j
            while 0 <= x+dir[0] < m and 0 <= y+dir[1] < n and\
                maze[x+dir[0]][y+dir[1]] != 1:
                x += dir[0]
                y += dir[1]
            result.add((x, y))
        result.discard((i, j))
        return list(result)
