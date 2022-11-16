# This is the solution for Maximum Slice Problem > Max Profit
#
# This is marked as PAINLESS difficulty

___ solution(A
    global_max_sum _ 0
    local_max_sum _ 0
    ___ i __ range(1, len(A)):
        d _ A[i] - A[i - 1]
        local_max_sum _ max(d, local_max_sum + d)
        global_max_sum _ max(local_max_sum, global_max_sum)
    r_ global_max_sum


#                      -2160,   112,   243,  -353,   354
print(solution([23171, 21011, 21123, 21366, 21013, 21367]))

