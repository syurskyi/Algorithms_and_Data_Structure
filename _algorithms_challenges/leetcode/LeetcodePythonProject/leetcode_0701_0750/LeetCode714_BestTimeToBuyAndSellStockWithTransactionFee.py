'''
Created on Oct 29, 2017

@author: MT
'''
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        buy = [0]*n
        sell = [0]*n
        buy[0] = -prices[0]
        for i in range(1, n):
            buy[i] = max(buy[i-1], sell[i-1]-prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i]-fee)
        return max(buy[-1], sell[-1])
    
    def test(self):
        testCases = [
            [
                [1, 3, 2, 8, 4, 9],
                2,
            ],
            [
                [1, 3, 7, 5, 10, 3],
                3,
            ],
        ]
        for prices, fee in testCases:
            print('prices: %s' % prices)
            print('fee: %s' % fee)
            result = self.maxProfit(prices, fee)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
