'''
Created on Feb 19, 2017

@author: MT
'''

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        degree = [0]*numCourses
        for p in prerequisites:
            graph[p[1]].append(p[0])
            degree[p[0]]+=1
        queue = []
        for num, cnt in enumerate(degree):
            if cnt == 0:
                queue.append(num)
        res = []
        count = 0
        while queue:
            node = queue.pop(0)
            res.append(node)
            count += 1
            for node0 in graph[node]:
                degree[node0] -= 1
                if degree[node0] == 0:
                    queue.append(node0)
        return res if count == numCourses else []
    
    def test(self):
        testCases = [
            [4, [[1,0],[2,0],[3,1],[3,2]]],
            [4, [[1,0],[2,0],[0,2],[3,1]]],
            [2, [[1,0]]],
        ]
        for numCourses, prerequisites in testCases:
            print('numCourses: %s' % (numCourses))
            print('prerequisites: %s' % (prerequisites))
            result = self.findOrder(numCourses, prerequisites)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
