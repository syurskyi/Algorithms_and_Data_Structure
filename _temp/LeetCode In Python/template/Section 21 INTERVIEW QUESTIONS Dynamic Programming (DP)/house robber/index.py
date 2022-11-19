c_ Solution
    ___ rob nums: List[i..]) __ i..:
        n _ l..(nums)
        __(n__0
            r_ 0
        
        dp _ [0] * n
        dp[0] _ nums[0]

        ___ i __ r..(1,n
            __(i__1
                dp[i] _ m__(nums[0],nums[1])
            ____
                dp[i] _ m__(dp[i-1], dp[i-2]+nums[i])
            
        r_ dp[-1]

        