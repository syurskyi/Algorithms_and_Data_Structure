c_ Solution:
    ___ longestPalindrome s: str) -> str:
        n _ l..(s)
        __(n<2
            r_ s
        left _ 0
        right _ 0

        palindrome _ [[0]*n ___ _ __ r..(n)]

        ___ j __ r..(1,n
            ___ i __ r..(0,j
                innerIsPalindrome _ palindrome[i+1][j-1] __ j-i<_2
                __(s[i] __ s[j] ___ innerIsPalindrome
                    palindrome[i][j] _ T..
                    __(j-i>right-left
                        left _ i
                        right _ j

        r_ s[left:right+1]
        