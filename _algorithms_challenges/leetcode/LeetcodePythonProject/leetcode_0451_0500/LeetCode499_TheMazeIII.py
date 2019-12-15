'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        m, n = len(maze), len(maze[0])
        result = []
        visited = [[False]*n for _ in range(m)]
        self.maxPath = float('inf')
        self.map = [[float('inf')]*n for _ in range(m)]
        self.helper(maze, ball, hole, '', 0, result, visited)
        result.sort(key=lambda x: (x[1], x[0]))
        if result:
            return result[0][0]
        else:
            return 'impossible'
    
    def helper(self, matrix, start, hole, curr, path, result, visited):
        if path > self.maxPath or path > self.map[start[0]][start[1]]:
            return
        nextSteps = self.getNextSteps(matrix, start[0], start[1])
        visited[start[0]][start[1]] = True
        self.map[start[0]][start[1]] = min(self.map[start[0]][start[1]], path)
        for step in nextSteps:
            stop = [step[0], step[1]]
            dirStr = step[2]
            dist = step[3]
            res, dist0 = self.isPassing(matrix, start, stop, hole)
            if res:
                self.maxPath = min(self.maxPath, path+dist0)
                result.append((curr+dirStr, path+dist0))
            elif not visited[stop[0]][stop[1]]:
                self.helper(matrix, stop, hole, curr+dirStr, path+dist, result, visited)
        visited[start[0]][start[1]] = False
    
    def isPassing(self, maze, start, stop, hole):
        if start[0] == stop[0] == hole[0]:
            if start[1] < hole[1] <= stop[1]:
                return True, hole[1]-start[1]
            elif stop[1] <= hole[1] < start[1]:
                return True, start[1]-hole[1]
        elif start[1] == stop[1] == hole[1]:
            if start[0] < hole[0] <= stop[0]:
                return True, hole[0]-start[0]
            elif stop[0] <= hole[0] < start[0]:
                return True, hole[0]-stop[0]
        return False, 0
    
    def getNextSteps(self, matrix, i, j):
        steps = set()
        m, n = len(matrix), len(matrix[0])
        dirs = (1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l')
        for dir in dirs:
            x, y = i, j
            dist = 0
            while 0 <= x+dir[0] < m and 0 <= y+dir[1] < n and\
                matrix[x+dir[0]][y+dir[1]] == 0:
                x += dir[0]
                y += dir[1]
                dir += 1
            if x != i or y != j:
                steps.add((x, y, dir[2], dist))
        return steps
