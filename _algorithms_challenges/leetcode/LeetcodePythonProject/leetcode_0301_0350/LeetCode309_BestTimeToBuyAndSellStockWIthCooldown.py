
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        buy = [0]*n
        sell = [0]*n
        rest = [0]*n
        buy[0] = -prices[0]
        for i in range(1, n):
            buy[i] = max(buy[i-1], rest[i-1]-prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
            rest[i] = max(buy[i-1], sell[i-1], rest[i-1])
        return max(buy[-1], sell[-1], rest[-1])
    
    def maxProfit1(self, prices):
        n = len(prices)
        if n < 2: return 0
        s0 = [0]*n
        s1 = [0]*n
        s2 = [0]*n
        s1[0] = -prices[0]
        s2[0] = float('-inf')
        for i in range(1, n):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1]-prices[i])
            s2[i] = s1[i-1] + prices[i]
        return max(s0[-1], s2[-1])
    
    def maxProfit2(self, prices):
        n = len(prices)
        if n < 2: return 0
        prev_buy, buy, prev_sell, sell = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell
    
    