# This is the solution for Prime And Composite > Flags
#
# This is marked as RESPECTABLE difficulty


___ solution(A
    peaks _ [0] * len(A)
    next_peak _ len(A)
    peaks[len(A) - 1] _ next_peak
    ___ i __ range(len(A) - 2, 0, -1
        __ A[i - 1] < A[i] and A[i + 1] < A[i]:
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
    ___ i __ range(flags_to_place
        __ current_position + flags_to_place > len(peaks) - 1:
            r_ False
        current_position _ peaks[current_position + flags_to_place]
    r_ current_position < len(peaks)


test_trail _ [1,5,3,4,3,4,1,2,3,4,6,2]
print(solution(test_trail))

