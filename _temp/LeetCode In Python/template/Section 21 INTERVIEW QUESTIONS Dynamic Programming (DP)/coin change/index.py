c_ Solution:
    ___ coinChange coins: List[int], amount: int) -> int:
        __ amount <_ 0:
            r_ 0
        
        __ min(coins) > amount:
            r_ -1

        INT_MAX _ 1<<32
        dp _ [INT_MAX] * (amount +1)
        
        dp[0] _ 0
        
        ___ i __ range(1, amount + 1
            ___ coin __ coins:
                __ coin <_ i:
                    dp[i] _ min((dp[i-coin] + 1), dp[i])
                    
        r_ dp[amount] __ dp[amount] !_ INT_MAX else -1