c_ Solution:
    ___ isPalin seg
        i _ 0
        j _ len(seg)-1
        _____(i < j
            __(seg[i] !_ seg[j]
                r_ False
            i +_ 1
            j -_ 1
        r_ True

    ___ dfs s: str
        __(len(s) == 0 and len(temp) > 0
            res.append(temp[:])
            r_
        n _ len(s)+1
        ___ i __ range(1, n
            seg _ s[0:i]
            __(isPalin(seg)):
                temp.append(seg)
                dfs(s[i:])
                temp.pop()

    ___ partition s: str) -> List[List[str]]:
        res _ []
        temp _ []
        dfs(s)
        r_ res
