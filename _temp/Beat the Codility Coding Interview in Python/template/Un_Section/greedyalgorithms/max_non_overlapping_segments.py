# This is the solution for Greedy algorithms > MaxNonoverlappingSegments
# The problem is equivalent to the Activity Selection Problem,
# where you have to choose the maximum non overlapping tasks.
#
# This is marked as PAINLESS difficulty

___ solution(A, B
    last_end_segment _ -1
    chosen_count _ 0
    ___ i __ range(l..(A)):
        __ A[i] > last_end_segment:
            chosen_count +_ 1
            last_end_segment _ B[i]
    r_ chosen_count



print(solution([1, 3, 7, 9, 1], [5, 6, 8, 9, 10]))

print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))

print(solution(   # list, []))
