'''
Created on Oct 15, 2019

@author: tongq
'''
class Solution(object):
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        import heapq
        graph = [[-1]*N for _ in range(N)]
        for edge in edges:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]
        res = 0
        h = []
        visited = [False]*N
        heapq.heappush(h, (-M, 0))
        while h:
            cur = heapq.heappop(h)
            start = cur[1]
            move = -cur[0]
            if visited[start]:
                continue
            visited[start] = True
            res += 1
            for i in range(N):
                if graph[start][i] != -1:
                    if move > graph[start][i] and not visited[i]:
                        heapq.heappush(h, ( -(move-graph[start][i]-1), i) )
                    graph[i][start] -= min(move, graph[start][i])
                    res += min(move, graph[start][i])
        return res
