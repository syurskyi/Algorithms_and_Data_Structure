c_ Solution
    ___ reverseString s
        """
        Do not return anything, modify s in-place instead.
        """

        left _ 0
        right _ l..(s) - 1

        _____ left < right:
            s[left], s[right] _ s[right], s[left]
            left +_ 1
            right -_ 1