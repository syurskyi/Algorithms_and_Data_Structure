# This is the solution for Arrays > CyclicRotation
#
# This is marked as PAINLESS difficulty

___ solution(A, K
    result _ [N..] * l..(A)

    ___ i __ range(l..(A)):
        result[(i + K) % l..(A)] _ A[i]

    r_ result

print(solution([1, 2, 3, 4, 5], 2))

print(solution([1, 2, 3, 4, 5], 5))
