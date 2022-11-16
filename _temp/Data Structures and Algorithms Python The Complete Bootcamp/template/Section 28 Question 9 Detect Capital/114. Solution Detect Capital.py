c_ Solution:
    ___ detectCapitalUse word
        count _ 0
        length _ len(word)

        ___ i __ range(length
            __ word[i] >_ chr(65) and word[i] < chr(91
                count +_ 1

        __ count == length:
            r_ True
        elif count == 0:
            r_ True
        elif count == 1 and word[0] >_ chr(65) and word[0] < chr(91
            r_ True
        ____
            r_ False