c_ Solution:
    ___ trap height: List[i..]) -> i..:
        n _ l..(height)
        __(n __ 0
            r_ 0

        left _ [0]*n
        right _ [0] * n

        ans _ 0

        left[0] _ height[0]

        ___ i __ r..(1, n
            left[i] _ m__(left[i-1], height[i])

        right[n-1] _ height[n-1]

        ___ i __ r..(n-2, -1, -1
            right[i] _ m__(right[i+1], height[i])

        ___ i __ r..(0, n
            ans +_ min(left[i], right[i])-height[i]

        r_ ans
