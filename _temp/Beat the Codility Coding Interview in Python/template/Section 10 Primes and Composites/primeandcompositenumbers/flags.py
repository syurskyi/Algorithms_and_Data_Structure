# This is the solution for Prime And Composite > Flags
#
# This is marked as RESPECTABLE difficulty


___ solution(A
    peaks _ [0] * l..(A)
    next_peak _ l..(A)
    peaks[l..(A) - 1] _ next_peak
    ___ i __ r..(l..(A) - 2, 0, -1
        __ A[i - 1] < A[i] ___ A[i + 1] < A[i]:
            next_peak _ i
        peaks[i] _ next_peak
    peaks[0] _ next_peak

    current_guess _ 0
    next_guess _ 0
    _____ can_place_flags(peaks, next_guess
        current_guess _ next_guess
        next_guess +_ 1
    r_ current_guess


___ can_place_flags(peaks, flags_to_place
    current_position _ 1 - flags_to_place
    ___ i __ r..(flags_to_place
        __ current_position + flags_to_place > l..(peaks) - 1:
            r_ F..
        current_position _ peaks[current_position + flags_to_place]
    r_ current_position < l..(peaks)


test_trail _ [1,5,3,4,3,4,1,2,3,4,6,2]
print(solution(test_trail))

