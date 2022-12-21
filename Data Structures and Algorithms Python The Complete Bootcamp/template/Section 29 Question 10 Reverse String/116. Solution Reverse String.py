c_ Solution:
    ___ reverseString  s):
        """
        Do not return anything, modify s __-place instead.
        """

        left = 0
        right = len(s) - 1

        ______ left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1