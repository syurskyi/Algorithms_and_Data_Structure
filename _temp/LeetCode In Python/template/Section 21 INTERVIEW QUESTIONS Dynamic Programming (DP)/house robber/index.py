c_ Solution:
    ___ rob nums: List[int]) -> int:
        n _ len(nums)
        __(n==0
            r_ 0
        
        dp _ [0] * n
        dp[0] _ nums[0]

        ___ i __ range(1,n
            __(i==1
                dp[i] _ max(nums[0],nums[1])
            ____
                dp[i] _ max(dp[i-1], dp[i-2]+nums[i])
            
        r_ dp[-1]

        