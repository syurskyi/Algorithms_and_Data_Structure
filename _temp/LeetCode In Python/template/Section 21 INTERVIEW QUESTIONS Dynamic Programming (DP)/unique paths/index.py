c_ Solution:
    ___ uniquePaths m: int, n: int) -> int:
        
        dp _ [[0 ___ x __ range(m)] ___ y __ range(n)]
        ___ i __ range(m
            dp[0][i] _ 1
        
        ___ i __ range(n
            dp[i][0] _ 1
        
        ___ i __ range(1, n
            ___ j __ range(1, m
                dp[i][j] _ dp[i-1][j] + dp[i][j-1]
        
        r_(dp[-1][-1])