'''
Created on May 11, 2017

@author: MT
'''

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        import heapq
        if not maze or not maze[0]: return -1
        m, n = len(maze), len(maze[0])
        heap = []
        heapq.heappush(heap, (0, start[0], start[1]))
        visited = [[False]*n for _ in range(m)]
        while heap:
            currDist, i, j = heapq.heappop(heap)
            if i == destination[0] and j == destination[1]:
                return currDist
            visited[i][j] = True
            for x, y, dist in self.getNextSteps(maze, i, j):
                if not visited[x][y]:
                    heapq.heappush(heap, (currDist+dist, x, y))
        return -1
    
    def getNextSteps(self, maze, i, j):
        m, n = len(maze), len(maze[0])
        steps = set()
        dirs = (1, 0), (0, 1), (-1, 0), (0, -1)
        for dir in dirs:
            x, y = i, j
            dist = 0
            while 0 <= x+dir[0] < m and 0 <= y+dir[1] < n and\
                maze[x+dir[0]][y+dir[1]] != 1:
                x += dir[0]
                y += dir[1]
                dist += 1
            if x != i or y != j:
                steps.add((x, y, dist))
        return list(steps)