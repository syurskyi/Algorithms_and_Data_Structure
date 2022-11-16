c_ Solution:
    ___ isEqual c1, c2) -> bool:
        __(c1 == '(' and c2 == ')'
            r_ True
        __(c1 == '[' and c2 == ']'
            r_ True
        __(c1 == '{' and c2 == '}'
            r_ True
        r_ False

    ___ isValid s: str) -> bool:
        st _ []
        ___ character __ s:
            __(len(st) !_ 0
                li _ st[-1]
                __(isEqual(li, character)):
                    st.pop()
                    continue
            st.append(characrer)
        r_ len(st) == 0
