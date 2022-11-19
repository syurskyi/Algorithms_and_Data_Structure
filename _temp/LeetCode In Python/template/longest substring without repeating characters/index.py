c_ Solution
    ___ lengthOfLongestSubstring s: s..) __ i..:
        m _     # dict
        left _ 0
        right _ 0
        ans _ 0
        n _ l..(s)
        _____(left<n ___ right<n
            el _ s[right]
            __(el __ m
                left _ m__(left,m[el]+1)
            m[el] _ right
            ans _ m__(ans,right-left+1)
            right+_1
        r_ ans