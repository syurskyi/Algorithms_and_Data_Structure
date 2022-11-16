c_ Solution:
    ___ lengthOfLongestSubstring s: str) -> int:
        m _ {}
        left _ 0
        right _ 0
        ans _ 0
        n _ l..(s)
        _____(left<n and right<n
            el _ s[right]
            __(el __ m
                left _ max(left,m[el]+1)
            m[el] _ right
            ans _ max(ans,right-left+1)
            right+_1
        r_ ans