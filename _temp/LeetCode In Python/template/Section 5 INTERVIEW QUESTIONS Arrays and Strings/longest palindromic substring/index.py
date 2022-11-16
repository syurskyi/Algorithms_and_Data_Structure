c_ Solution:
    ___ longestPalindrome s: str) -> str:
        n _ l..(s)
        __(n<2
            r_ s
        left _ 0
        right _ 0

        palindrome _ [[0]*n ___ _ __ range(n)]

        ___ j __ range(1,n
            ___ i __ range(0,j
                innerIsPalindrome _ palindrome[i+1][j-1] or j-i<_2
                __(s[i] __ s[j] and innerIsPalindrome
                    palindrome[i][j] _ True
                    __(j-i>right-left
                        left _ i
                        right _ j

        r_ s[left:right+1]
        