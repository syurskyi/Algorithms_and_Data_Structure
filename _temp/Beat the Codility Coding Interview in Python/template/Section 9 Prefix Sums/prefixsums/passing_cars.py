# This is the solution for Prefix Sums > Passing Cars
#
# This is marked as PAINLESS difficulty

___ solution(A
    suffix_sum _ [0] * (len(A) + 1)
    ___ i __ range(len(A) - 1, -1, -1
        suffix_sum[i] _ A[i] + suffix_sum[i + 1]

    count _ 0
    ___ i __ range(len(A)):
        __ A[i] == 0:
            count +_ suffix_sum[i]
        __ count > 1000000000:
            r_ -1

    r_ count


print(solution([0, 1, 0, 1, 1]))
