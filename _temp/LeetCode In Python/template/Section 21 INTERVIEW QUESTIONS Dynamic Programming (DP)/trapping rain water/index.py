c_ Solution:
    ___ trap height: List[int]) -> int:
        n _ len(height)
        __(n == 0
            r_ 0

        left _ [0]*n
        right _ [0] * n

        ans _ 0

        left[0] _ height[0]

        ___ i __ range(1, n
            left[i] _ max(left[i-1], height[i])

        right[n-1] _ height[n-1]

        ___ i __ range(n-2, -1, -1
            right[i] _ max(right[i+1], height[i])

        ___ i __ range(0, n
            ans +_ min(left[i], right[i])-height[i]

        r_ ans
