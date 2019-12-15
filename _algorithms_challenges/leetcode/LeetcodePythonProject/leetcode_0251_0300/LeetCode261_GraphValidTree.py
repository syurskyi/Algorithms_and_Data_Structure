'''
Created on Mar 2, 2017

@author: MT
'''

class Solution(object):
    def validTree(self, n, edges):
        roots = [-1]*n
        for e in edges:
            root0 = self.findRoot(roots, e[0])
            root1 = self.findRoot(roots, e[1])
            if root0 != root1:
                roots[root0] = root1
            else:
                return False
        return len(edges) == n-1
    
    def findRoot(self, roots, ind):
        while roots[ind] != -1:
            ind = roots[ind]
        return ind
    
    def validTreeBFS(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        hashmap = {}
        for i in range(n):
            hashmap[i] = []
        for edge in edges:
            hashmap[edge[0]].append(edge[1])
            hashmap[edge[1]].append(edge[0])
        queue = []
        queue.append(0)
        visited = [False]*n
        while queue:
            top = queue[0]
            queue.pop(0)
            if visited[top]:
                return False
            visited[top] = True
            for i in hashmap[top]:
                if not visited[i]:
                    queue.append(i)
        for b in visited:
            if not b:
                return False
        return True
    
    def validTreeDFS(self, n, edges):
        hashmap = {}
        for i in range(n):
            hashmap[i] = []
        for edge in edges:
            hashmap[edge[0]].append(edge[1])
            hashmap[edge[1]].append(edge[0])
        visited = [False]*n
        if not self.helper(0, -1, hashmap, visited):
            return False
        for b in visited:
            if not b: return False
        return True
    
    def helper(self, curr, parent, hashmap, visited):
        if visited[curr]: return False
        visited[curr] = True
        for i in hashmap[curr]:
            if i != parent and not self.helper(i, curr, hashmap, visited):
                return False
        return True
    
    def test(self):
        testCases = [
            (
                5,
                [[0, 1], [0, 2], [0, 3], [1, 4]],
            ),
            (
                5,
                [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]],
            ),
            [
                6,
                [[0,1],[1,2],[2,0],[3,4],[4,5]],
            ],
        ]
        for n, edges in testCases:
            print('n: %s' % (n))
            print('edges: %s' % (edges))
            result = self.validTree(n, edges)
            print('result: %s' % (result))
            print('-='*20+'-')
        
if __name__ == '__main__':
    Solution().test()
