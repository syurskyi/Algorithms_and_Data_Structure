c_ Solution:
    ___ isEqual c1, c2) -> bool:
        __(c1 __ '(' ___ c2 __ ')'
            r_ T..
        __(c1 __ '[' ___ c2 __ ']'
            r_ T..
        __(c1 __ '{' ___ c2 __ '}'
            r_ T..
        r_ F..

    ___ isValid s: str) -> bool:
        st _    # list
        ___ character __ s:
            __(l..(st) !_ 0
                li _ st[-1]
                __(isEqual(li, character
                    st.p.. 
                    continue
            st.a..(characrer)
        r_ l..(st) __ 0
