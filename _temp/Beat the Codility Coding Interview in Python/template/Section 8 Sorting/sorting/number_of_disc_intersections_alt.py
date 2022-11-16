# This is the solution for Sorting > NumberOfDiscIntersections
#
# This is marked as RESPECTABLE difficulty

c_ Disc(
    ___ -  low_x, high_x
        low_x _ low_x
        high_x _ high_x

___ index_less_than(sortedDiscList, i, start, last
    mid _ start + (last - start) // 2
    __ last <_ start ___ sortedDiscList[mid].low_x > i:
        r_ mid - 1
    ____ last <_ start:
        r_ mid
    ____ sortedDiscList[mid].low_x > i:
        r_ index_less_than(sortedDiscList, i, start, mid - 1)
    ____
        r_ index_less_than(sortedDiscList, i, mid + 1, last)

___ solution(A
    discs _    # list
    ___ i __ r..(l..(A
        discs.a..(Disc(i - A[i], i + A[i]))
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
