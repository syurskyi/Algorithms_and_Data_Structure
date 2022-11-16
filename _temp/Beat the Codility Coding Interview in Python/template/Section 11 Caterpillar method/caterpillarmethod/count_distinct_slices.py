# This is the solution for Caterpillar Method > CountDistinctSlices
#
# This is marked as PAINLESS difficulty

___ solution(M, A
    total_slices _ 0
    in_current_slice _ [F..] * (M + 1)
    head _ 0
    ___ tail __ r..(0,l..(A
        _____ head < l..(A) ___ (n.. in_current_slice[A[head]]
            in_current_slice[A[head]] _ T..
            total_slices +_ (head - tail) + 1
            head +_ 1
            total_slices _ 1000000000 __ total_slices > 1000000000 ____ total_slices
        in_current_slice[A[tail]] _ F..
    r_ total_slices


print(solution(9, [2, 4, 1, 7, 4, 9, 7, 3, 5, 5, 8, 7, 1]))

print(solution(6, [3, 4, 5, 5, 2]))

