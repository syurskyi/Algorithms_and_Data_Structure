'''
Created on Feb 14, 2017

@author: MT
'''

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        tbl = [[0]*n for _ in range(m)]
        if dungeon[-1][-1] > 0:
            tbl[-1][-1] = 1
        else:
            tbl[-1][-1] = 1-dungeon[-1][-1]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if i == m-1:
                    right = tbl[i][j+1] - dungeon[i][j]
                    tbl[i][j] = max(1, right)
                if j == n-1:
                    down = tbl[i+1][j] - dungeon[i][j]
                    tbl[i][j] = max(1, down)
                if i != m-1 and j != n-1:
                    right = tbl[i][j+1] - dungeon[i][j]
                    down = tbl[i+1][j] - dungeon[i][j]
                    tbl[i][j] = max(1, min(right, down))
        return tbl[0][0]
