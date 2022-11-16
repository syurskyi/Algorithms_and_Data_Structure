c_ MinStack:
    ___ -
        st _ []

    ___ push x: int) -> N..:
        curMin _ getMin()
        __ curMin == N.. or curMin > x:
            curMin _ x
        st.append((x, curMin))

    ___ pop ) -> N..:
        st.pop()

    ___ top ) -> int:
        r_ st[-1][0] __ st else N..

    ___ getMin ) -> int:
        r_ st[-1][1] __ st else N..
