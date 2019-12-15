'''
Created on Mar 3, 2017

@author: MT
'''

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        minInd1, minInd2 = -1, -1
        for i in range(n):
            last1, last2 = minInd1, minInd2
            minInd1, minInd2 = -1, -1
            for j in range(k):
                if j != last1:
                    costs[i][j] += 0 if last1 < 0 else costs[i-1][last1]
                else:
                    costs[i][j] += 0 if last2 < 0 else costs[i-1][last2]
                if minInd1 < 0 or costs[i][j] < costs[i][minInd1]:
                    minInd2 = minInd1
                    minInd1 = j
                elif minInd2 < 0 or costs[i][j] < costs[i][minInd2]:
                    minInd2 = j
        return costs[-1][minInd1]
    
    def minCostII_slow(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        n = len(costs)
        k = len(costs[0])
        for i in range(1, n):
            for j in range(k):
                minList = []
                for l in range(k):
                    if j != l:
                        minList.append(costs[i-1][l])
                costs[i][j] += min(minList)
        return min(costs[-1])
    
    def test(self):
        testCases = [
            [[1,5,3],[2,9,4]],
        ]
        for costs in testCases:
            print('costs: %s' % costs)
            result = self.minCostII(costs)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
