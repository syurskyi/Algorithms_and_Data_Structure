c_ PlateStack:

    ___ -  
        st _ []

    ___ push x: int) -> N..:
        st.append(x)

    ___ pop ) -> N..:
        __(len(st) > 0
            st.pop()

    ___ top ) -> int:
        __(len(st) == 0
            r_ N..
        r_ st[-1]

    ___ getLen ) -> int:
      r_ len(st)