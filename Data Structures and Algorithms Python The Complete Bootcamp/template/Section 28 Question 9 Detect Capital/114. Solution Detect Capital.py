c_ Solution:
    ___ detectCapitalUse  word):
        count = 0
        length = len(word)

        ___ i __ r..(length):
            __ word[i] >= chr(65) and word[i] < chr(91):
                count += 1

        __ count __ length:
            r_ True
        ____ count __ 0:
            r_ True
        ____ count __ 1 and word[0] >= chr(65) and word[0] < chr(91):
            r_ True
        ____
            r_ False