c_ Solution:
    ___ isPalin seg
        i _ 0
        j _ l..(seg)-1
        _____(i < j
            __(seg[i] !_ seg[j]
                r_ F..
            i +_ 1
            j -_ 1
        r_ T..

    ___ dfs s: str
        __(l..(s) __ 0 ___ l..(temp) > 0
            res.a..(temp[:])
            r_
        n _ l..(s)+1
        ___ i __ r..(1, n
            seg _ s[0:i]
            __(isPalin(seg
                temp.a..(seg)
                dfs(s[i:])
                temp.p.. 

    ___ partition s: str) -> List[List[str]]:
        res _    # list
        temp _    # list
        dfs(s)
        r_ res
