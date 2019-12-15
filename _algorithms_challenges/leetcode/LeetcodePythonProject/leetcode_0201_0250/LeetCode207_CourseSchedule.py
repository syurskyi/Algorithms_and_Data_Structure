'''
Created on Feb 18, 2017

@author: MT
'''

class Solution(object):
    def canFinishBFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        degree = [0]*numCourses
        queue = []
        count = 0
        for prereq in prerequisites:
            degree[prereq[0]] += 1
            graph[prereq[1]].append(prereq[0])
        print('degree: %s' % (degree))
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
                count += 1
        while queue:
            course = queue.pop(0)
            for pointer in graph[course]:
                degree[pointer] -= 1
                if degree[pointer] == 0:
                    queue.append(pointer)
                    count += 1
        print('graph:  %s' % (graph))
        print('degree: %s' % (degree))
        if count == numCourses:
            return True
        else:
            return False
    
    def canFinishDFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [False]*numCourses
        for i, prereq in enumerate(prerequisites):
            graph[prereq[1]].append(prereq[0])
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, course):
        if visited[course]:
            return False
        else:
            visited[course] = True
        for precourse in graph[course]:
            if not self.dfs(graph, visited, precourse):
                return False
        visited[course] = False
        return True
    
    def test(self):
        testCases = [
            (2, [[1, 0]]),
            (5, [[0, 1], [1, 2], [2, 3]]),
            (6, [[0, 2], [2, 1], [1, 3]]),
            (5, [[0, 1], [1, 2], [2, 3], [4, 1], [4, 2], [4, 0], [1, 4]]),
            (3, [[0, 1], [1, 0], [2, 0]]),
        ]
        for numCourses, prerequisites in testCases:
            print('numCourses: %s' % (numCourses))
            print('prerequisites: %s' % (prerequisites))
            result = self.canFinishDFS(numCourses, prerequisites)
            print('DFS Result: %s' % (result))
            result = self.canFinishBFS(numCourses, prerequisites)
            print('BFS Result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()