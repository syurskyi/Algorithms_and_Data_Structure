'''
Created on Apr 10, 2019

@author: tongq
'''

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        queue = []
        hashset = set()
        
        for i in range(n):
            tmp = (1 << i)
            hashset.add((tmp, i, 0))
            queue.append((tmp, i, 1))
        
        while queue:
            curr = queue.pop(0)
            if curr[0] == (1 << n)-1:
                return curr[2]-1
            else:
                neighbors = graph[curr[1]]
                for v in neighbors:
                    bitMask = curr[0]
                    bitMask |= (1<<v)
                    t = (bitMask, v, 0)
                    if t not in hashset:
                        queue.append((bitMask, v, curr[2]+1))
                        hashset.add(t)
        return -1
    
    def test(self):
        testCases = [
            [[1,2,3],[0],[0],[0]],
            [[1],[0,2,4],[1,3,4],[2],[1,2]],
        ]
        for graph in testCases:
            result = self.shortestPathLength(graph)
            print('result: %s' % result)

if __name__ == '__main__':
    Solution().test()
