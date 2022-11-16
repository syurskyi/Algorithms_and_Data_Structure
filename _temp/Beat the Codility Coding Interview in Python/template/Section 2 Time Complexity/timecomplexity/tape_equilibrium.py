# This is the solution for Time Complexity > TapeEquilibrium
#
# This is marked as PAINLESS difficulty

___ solution(A
    sum_left _ A[0]
    sum_right _ sum(A) - A[0]
    diff _ abs(sum_left - sum_right)
    ___ i __ range(1, l..(A)-1
        sum_left +_ A[i]
        sum_right -_ A[i]
        current_diff _ abs(sum_left - sum_right)
        __ diff > current_diff:
            diff _ current_diff
    r_ diff


print(solution([3, 1, 2, 4, 3]))


