c_ MinStack:
    ___ -
        st _    # list

    ___ push x: int) -> N..:
        curMin _ getMin()
        __ curMin __ N.. __ curMin > x:
            curMin _ x
        st.a..((x, curMin))

    ___ pop ) -> N..:
        st.p.. 

    ___ top ) -> int:
        r_ st[-1][0] __ st ____ N..

    ___ getMin ) -> int:
        r_ st[-1][1] __ st ____ N..
