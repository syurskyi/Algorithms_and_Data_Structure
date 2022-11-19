c_ Solution

    ___ longestPalindrome s
        result _ ""
        ___ i __ r..(l..(s
            word1 _ checkPalindrome(s, i, i)
            word2 _ checkPalindrome(s, i, i + 1)

            __ l..(word1) >_ l..(word2
                longest _ word1
            ____
                longest _ word2

            __ l..(longest) >_ l..(result
                result _ longest
            ____
                result _ result

        r_ result

    ___ checkPalindrome s, left, right

        _____ left >_ 0 ___ right < l..(s) ___ s[left] __ s[right]:
            left -_ 1
            right +_ 1

        r_ s[left + 1:right]