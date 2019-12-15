'''
Created on Apr 18, 2018

@author: tongq
'''
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        result = [[0.0]*101 for _ in range(101)]
        result[0][0] = poured
        for i in range(100):
            for j in range(i+1):
                if result[i][j] >= 1:
                    result[i+1][j] += (result[i][j]-1)/2.0
                    result[i+1][j+1] += (result[i][j]-1)/2.0
                    result[i][j] = 1.0
        return result[query_row][query_glass]
    
    def test(self):
        testCases = [
            [1, 1, 1], # 0.0
            [2, 1, 1], # 0.5
            [2, 1, 0], # 0.5
            [6, 2, 0],
            [6, 2, 1],
            [6, 3, 1],
            [6, 3, 0]
        ]
        for poured, query_row, query_glass in testCases:
            print('poured: %s' % poured)
            print('query_row: %s' % query_row)
            print('query_glass: %s' % query_glass)
            result = self.champagneTower(poured, query_row, query_glass)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
