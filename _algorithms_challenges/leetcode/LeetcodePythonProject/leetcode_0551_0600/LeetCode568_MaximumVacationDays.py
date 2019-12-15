'''
Created on Sep 3, 2017

@author: MT
'''

class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        n = len(flights)
        k0 = len(days[0])
        dp = [float('-inf')]*n
        dp[0] = 0
        for i in range(k0):
            tmp = [float('-inf')]*n
            for j in range(n):
                for k in range(n):
                    if j == k or flights[k][j] == 1:
                        tmp[j] = max(tmp[j], dp[k]+days[j][i])
            dp = tmp
        return max(dp)
    
    def test(self):
        testCases = [
            [
                [
                    [0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0],
                ],
                [
                    [1, 3, 1],
                    [6, 0, 3],
                    [3, 3, 3],
                ],
            ],
            [
                [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                ],
                [
                    [1, 1, 1],
                    [7, 7, 7],
                    [7, 7, 7],
                ],
            ],
            [
                [
                    [0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0],
                ],
                [
                    [7, 0, 0],
                    [0, 7, 0],
                    [0, 0, 7],
                ],
            ],
        ]
        for flights, days in testCases:
            print('flights:')
            print('\n'.join([str(row) for row in flights]))
            print('days:')
            print('\n'.join([str(row) for row in days]))
            result = self.maxVacationDays(flights, days)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
