c_ Solution:
    ___ climbStairs n: i..) -> i..:
        __(n __ 1
            r_ 1
        dp _ [0]*(n+1)
        dp[1] _ 1
        dp[2] _ 2

        ___ i __ r..(3, n+1
            dp[i] _ dp[i-1]+d[i-2]

        r_ dp[n]
