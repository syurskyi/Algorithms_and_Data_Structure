# This is the solution for Sorting > NumberOfDiscIntersections
#
# This is marked as RESPECTABLE difficulty

c_ Disc
    ___ -  low_x, high_x
        ? _ ?
        ? _ ?

___ index_less_than(sortedDiscList, i, start, last
    mid _ ? + (l.. - ?) // 2
    __ l.. <_ ? ___ ? ?.l.. > i
        r_ ? - 1
    ____ l.. <_ ?
        r_ ?
    ____ ? ?.l.. > i
        r_ ? ? ?, s.., ? - 1
    ____
        r_ ? ? ?, ? + 1, l..

___ solution A
    discs _    # list
    ___ i __ r..(l.. ?
        ?.a..(?(i - A[i], i + A[i]))
    discs _ s..(discs, key_lambda d: d.low_x)
    total _ 0
    ___ i __ r..(l..(discs
        total +_ index_less_than(discs, discs[i].high_x + 0.5, 0, l..(discs) - 1) - i
        __ total > 10000000:
            total _ -1
            b..
    r_ total

print(solution([1, 5, 2, 1, 4, 0]))

print(solution([0] * 100000))
