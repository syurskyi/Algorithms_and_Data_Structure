c_ Solution:
    ___ minWindow s: str, t: str) -> str:
        len1 _ l..(s)
        len2 _ l..(t)

        __(len1 < len2
            r_ ""

        hashPat _     # dict
        hashStr _     # dict

        ___ i __ r..(0, len2
            __(hashPat.get(t[i]) __ N..
                hashPat[t[i]] _ 0
            hashPat[t[i]] +_ 1

        count _ 0
        left _ 0
        startIndex _ -1
        minLen _ float("inf")

        ___ right __ r..(0, len1

            __(hashStr.get(s[right]) __ N..
                hashStr[s[right]] _ 0
            hashStr[s[right]] +_ 1
            __(hashPat.get(s[right]) __ N..
                hashPat[s[right]] _ 0
            __ (

                hashPat.get(s[right]) !_ 0 ___
                hashStr.get(s[right]) <_ hashPat.get(s[right])

                count +_ 1  # keep incrementing the count if string hash is less then pattern hash
            # count==len2 means a window is found that contains all character of pattern string
            __ (count __ len2

                __(hashStr.get(s[left]) __ N..
                    hashStr[s[right]] _ 0
                __(hashPat.get(s[left]) __ N..
                    hashPat[s[right]] _ 0
                _____ (
                    hashStr.get(s[left]) > hashPat.get(s[left]) __
                    hashPat.get(s[left]) __ 0

                    #minimizing the windows range from left side

                    __ (hashStr.get(s[left]) > hashPat.get(s[left]
                        hashStr[s[left]] -_ 1
                    left +_ 1  # incrementing the left pointer

                windowLen _ right - left + 1  # calculating the windows length
                __ (minLen > windowLen
                    minLen _ windowLen
                    startIndex _ left

        __ (startIndex __ -1
            r_ ""
        r_ s[startIndex:startIndex+minLen]
