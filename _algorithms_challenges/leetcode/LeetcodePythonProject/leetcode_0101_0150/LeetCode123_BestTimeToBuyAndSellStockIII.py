'''
Created on Feb 6, 2017

@author: MT
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1: return 0
        left = [0]*len(prices)
        right = [0]*len(prices)
        minVal = prices[0]
        for i in range(1, len(prices)):
            left[i] = max(prices[i]-minVal, left[i])
            minVal = min(minVal, prices[i])
        maxVal = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            right[i] = max(maxVal-prices[i], right[i+1])
            maxVal = max(maxVal, prices[i])
        profit = 0
        for i in range(len(prices)):
            profit = max(left[i]+right[i], profit)
        return profit
    
    def test(self):
        testCases = [
            [1, 9, 2, 1, 3, 7, 2],
            [1, 7, 2, 9, 3, 1, 10],
            [1, 2],
            [2, 1],
            [3, 3],
        ]
        for prices in testCases:
            print('prices: %s' % (prices))
            result = self.maxProfit(prices)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()