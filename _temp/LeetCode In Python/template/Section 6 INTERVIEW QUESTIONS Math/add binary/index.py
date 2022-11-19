c_ Solution o..
    ___ addBinary a, b
        result _    # list
        carry _ 0
        i _ l..(a)-1
        j _ l..(b)-1

        _____ i >_ 0 __ j >_ 0 __ carry:
            total _ carry

            __ i >_ 0:
                total +_ i..(a[i])
                i -_ 1
            __ j >_ 0:
                total +_ i..(b[j])
                j -_ 1

            result.a..(s..(total % 2))
            carry _ total//2

        r_ ''.j..(reversed(result))
