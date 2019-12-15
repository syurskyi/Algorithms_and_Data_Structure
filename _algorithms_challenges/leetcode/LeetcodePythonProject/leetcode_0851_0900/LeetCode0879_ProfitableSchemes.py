'''
Created on Oct 14, 2019

@author: tongq
'''
class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        dp = [[0]*(G+1) for _ in range(P+1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G-g, -1, -1):
                    dp[min(i+p, P)][j+g] += dp[i][j]
        return sum(dp[P])%(10**9 + 7)
    
    def profitableSchemes_DFS_TLE(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        res = [0]
        self.dfs(0, group, profit, G, P, [], 0, res)
        return res[0]
    
    def dfs(self, ind, group, profit, G, P, curGroup, curProfit, res):
        if curProfit >= P and sum(curGroup) <= G:
            res[0] += 1
        for i in range(ind, len(group)):
            curProfit += profit[i]
            curGroup.append(group[i])
            self.dfs(i+1, group, profit, G, P, curGroup, curProfit, res)
            curGroup.pop()
            curProfit -= profit[i]
    
    def test(self):
        testCases = [
            [
                5, 3, [2,2], [2,3]
            ],
            [
                10, 5, [2,3,5], [6,7,8]
            ],
        ]
        for G, P, group, profit in testCases:
            res = self.profitableSchemes(G, P, group, profit)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
