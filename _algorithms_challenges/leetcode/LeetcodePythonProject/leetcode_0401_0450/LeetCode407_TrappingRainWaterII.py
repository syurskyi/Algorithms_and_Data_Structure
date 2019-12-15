'''
Created on Apr 10, 2017

@author: MT
'''
class Solution(object):
    def trapRainWater(self, heightMap):
        import heapq
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        res = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                if 0<=x<m and 0<=y<n and not visited[x][y]:
                    res += max(0, height-heightMap[x][y])
                    heapq.heappush(heap, (max(height, heightMap[x][y]), x, y))
                    visited[x][y] = True
        return res
    
    def test(self):
        testCases = [
            [
                [1,4,3,1,3,2],
                [3,2,1,3,2,4],
                [2,3,3,2,3,1],
            ],
        ]
        for heightMap in testCases:
            print('heightMap:')
            print('\n'.join([str(row) for row in heightMap]))
            result = self.trapRainWater(heightMap)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
