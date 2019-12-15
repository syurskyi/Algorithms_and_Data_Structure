'''
Created on Feb 5, 2017

@author: MT
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
    
    def test(self):
        testCases = [
            [1, 9, 2, 1, 3, 7, 2],
            [1, 2],
            [2, 1],
            [3, 3],
        ]
        for prices in testCases:
            print('prices: %s' % prices)
            result = self.maxProfit(prices)
            print('result: %s' % (result))
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()