c_ Solution:
    ___ maxProfit prices: List[int]) -> int:
        buyPrice _ float("inf")
        profit _ 0

        ___ i, price __ enumerate(prices
            __(buyPrice > price
                buyPrice _ price
            ____
                profit _ m__(profit, price-buyPrice)

        r_ profit
