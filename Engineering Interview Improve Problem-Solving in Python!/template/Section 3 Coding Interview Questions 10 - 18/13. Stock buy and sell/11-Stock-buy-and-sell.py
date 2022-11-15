# [23,18,15,12,34,55,22,44] => (1 3) (4 5)
# Day when price drops (price < previous day) => sell the previous day
# BUY when price > previous day => BUY the previous day

def buy_sell(prices):
    buy = 0
    previous_price = 10000 #max int
    for index, price in enumerate(prices):
        if price < previous_price:
            if buy:
                print(buy, index - 1)
                buy = 0
        elif previous_price < price:
            if not buy:
                buy = index - 1
        previous_price = price
    if buy:
        print(buy, len(prices) - 1)
buy_sell([23,18,15,12,34,55,22,44])