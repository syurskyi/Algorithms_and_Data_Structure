'''
Created on Sep 9, 2019

@author: tongq
'''
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = len(quiet)
        richer2 = {}
        for i in range(n):
            richer2[i] = []
        for v in richer:
            richer2[v[1]].append(v[0])
        res = [-1 for i in range(n)]
        for i in range(n):
            self.dfs(i, quiet, richer2, res)
        return res
    
    def dfs(self, i, quiet, richer2, res):
        if (res[i] >= 0):
            return res[i]
        res[i] = i
        for j in richer2[i]:
            if quiet[res[i]] > quiet[self.dfs(j, quiet, richer2, res)]:
                res[i] = res[j]
        return res[i]
    
    def test(self):
        testCase = [
            [
                [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],
                [3,2,5,4,6,1,7,0],
            ],
        ]
        for richer, quiet in testCase:
            res = self.loudAndRich(richer, quiet)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
