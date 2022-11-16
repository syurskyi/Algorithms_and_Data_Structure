c_ Solution:
    ___ detectCapitalUse word
        count _ 0
        length _ l..(word)

        ___ i __ r..(length
            __ word[i] >_ chr(65) ___ word[i] < chr(91
                count +_ 1

        __ count __ length:
            r_ T..
        ____ count __ 0:
            r_ T..
        ____ count __ 1 ___ word[0] >_ chr(65) ___ word[0] < chr(91
            r_ T..
        ____
            r_ F..