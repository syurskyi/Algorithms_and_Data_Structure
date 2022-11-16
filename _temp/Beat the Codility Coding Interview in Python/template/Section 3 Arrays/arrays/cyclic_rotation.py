# This is the solution for Arrays > CyclicRotation
#
# This is marked as PAINLESS difficulty

___ solution(A, K
    result _ [N..] * len(A)

    ___ i __ range(len(A)):
        result[(i + K) % len(A)] _ A[i]

    r_ result

print(solution([1, 2, 3, 4, 5], 2))

print(solution([1, 2, 3, 4, 5], 5))
