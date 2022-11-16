# This is the solution for Sorting > NumberOfDiscIntersections
#
# This is marked as RESPECTABLE difficulty

c_ DiscLog(
    ___ -  x, start_end
        x _ x
        start_end _ start_end

___ solution(A
    discHistory _    # list
    ___ i __ range(l..(A)):
        discHistory.a..(DiscLog(i - A[i], 1))
        discHistory.a..(DiscLog(i + A[i], -1))
    discHistory.sort(key_lambda d: (d.x, -d.start_end))
    intersections _ 0
    active_intersections _ 0
    ___ log __ discHistory:
        active_intersections +_ log.start_end
        __ log.start_end > 0:
            intersections +_ active_intersections - 1
        __ intersections > 10000000:
            r_ -1
    r_ intersections

print(solution([1, 5, 2, 1, 4, 0]))

print(solution([0] * 100000))

