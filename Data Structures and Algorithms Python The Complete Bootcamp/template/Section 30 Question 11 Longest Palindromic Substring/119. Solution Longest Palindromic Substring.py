c_ Solution:

    ___ longestPalindrome  s):
        result = ""
        ___ i __ r.. l..(s)):
            word1 = checkPalindrome(s, i, i)
            word2 = checkPalindrome(s, i, i + 1)

            __ len(word1) >= len(word2):
                longest = word1
            ____
                longest = word2

            __ len(longest) >= len(result):
                result = longest
            ____
                result = result

        r_ result

    ___ checkPalindrome  s, left, right):

        ______ left >= 0 and right < len(s) and s[left] __ s[right]:
            left -= 1
            right += 1

        r_ s[left + 1:right]