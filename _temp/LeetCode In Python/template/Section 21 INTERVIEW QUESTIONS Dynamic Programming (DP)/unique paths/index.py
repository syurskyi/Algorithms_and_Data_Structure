c_ Solution:
    ___ uniquePaths m: i.., n: i..) -> i..:
        
        dp _ [[0 ___ x __ r..(m)] ___ y __ r..(n)]
        ___ i __ r..(m
            dp[0][i] _ 1
        
        ___ i __ r..(n
            dp[i][0] _ 1
        
        ___ i __ r..(1, n
            ___ j __ r..(1, m
                dp[i][j] _ dp[i-1][j] + dp[i][j-1]
        
        r_(dp[-1][-1])