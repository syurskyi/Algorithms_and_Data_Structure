c_ Solution:

    ___ longestPalindrome s
        result _ ""
        ___ i __ range(len(s)):
            word1 _ checkPalindrome(s, i, i)
            word2 _ checkPalindrome(s, i, i + 1)

            __ len(word1) >_ len(word2
                longest _ word1
            ____
                longest _ word2

            __ len(longest) >_ len(result
                result _ longest
            ____
                result _ result

        r_ result

    ___ checkPalindrome s, left, right

        _____ left >_ 0 and right < len(s) and s[left] == s[right]:
            left -_ 1
            right +_ 1

        r_ s[left + 1:right]