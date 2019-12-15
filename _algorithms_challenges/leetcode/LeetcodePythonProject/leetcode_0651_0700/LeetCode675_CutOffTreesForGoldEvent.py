'''
Created on Oct 16, 2017

@author: MT
'''
import heapq

class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not forest or not forest[0]: return 0
        m, n = len(forest), len(forest[0])
        heap = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(heap, (forest[i][j], i, j))
        sumVal = 0
        x, y = 0, 0
        while heap:
            h, i, j = heapq.heappop(heap)
            step = self.minStep(forest, x, y, i, j, h, m, n)
            if step < 0: return -1
            sumVal += step
            x, y = i, j
        return sumVal
    
    def minStep(self, forest, x, y, i, j, h, m, n):
        step = 0
        visited = [[False]*n for _ in range(m)]
        visited[x][y] = True
        queue = []
        queue.append((x, y))
        while queue:
            size = len(queue)
            for _ in range(size):
                i0, j0 = queue.pop(0)
                if i0 == i and j0 == j: return step
                for i1, j1 in (i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1):
                    if i1 < 0 or i1 >= m or j1 < 0 or j1 >= n or\
                        forest[i1][j1] == 0 or visited[i1][j1]:
                        continue
                    queue.append((i1, j1))
                    visited[i1][j1] = True
            step += 1
        return -1
    
    def test(self):
        testCases = [
            [
                [1,2,3],
                [0,0,4],
                [7,6,5],
            ],
            [
                [1,2,3],
                [0,0,0],
                [7,6,5],
            ],
            [
                [2,3,4],
                [0,0,5],
                [8,7,6],
            ],
            [
                [54581641,  64080174,   24346381,   69107959],
                [86374198,  61363882,   68783324,   79706116],
                [668150,    92178815,   89819108,   94701471],
                [83920491,  22724204,   46281641,   47531096],
                [89078499,  18904913,   25462145,   60813308],
            ],
        ]
        for forest in testCases:
            print('forest: %s' % forest)
            result = self.cutOffTree(forest)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
