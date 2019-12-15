'''
Created on Sep 24, 2019

@author: tongq
'''
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        numOfKeys = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        moves = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    starti = i
                    startj = j
                elif grid[i][j] in 'abcdef':
                    numOfKeys += 1
        deque = []
        deque.append([starti, startj, 0, '.@abcdef', 0])
        while deque:
            i, j, steps, keys, collectedKeys = deque.pop(0)
            if grid[i][j] in 'abcdef' and grid[i][j].upper() not in keys:
                keys += grid[i][j].upper()
                collectedKeys += 1
            if collectedKeys == numOfKeys:
                return steps
            for x, y in dirs:
                ni = i+x
                nj = j+y
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] in keys:
                    if (ni, nj, keys) not in moves:
                        moves.add((ni, nj, keys))
                        deque.append([ni, nj, steps+1, keys, collectedKeys])
        return -1
    
    def test(self):
        testCase = [
            
        ]
        for grid in testCase:
            res = self.shortestPathAllKeys(grid)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
