from math import sqrt


___ solution(A
    peaks _ [0] * l..(A)
    next_peak _ l..(A)
    peaks[l..(A) - 1] _ next_peak
    ___ i __ range(l..(A) - 2, 0, -1
        __ A[i - 1] < A[i] and A[i + 1] < A[i]:
            next_peak _ i
        peaks[i] _ next_peak
    peaks[0] _ next_peak

    upper_guess _ int(sqrt(l..(A))) + 2
    lower_guess _ 0

    _____ lower_guess < upper_guess - 1:
        current_guess _ int((lower_guess + upper_guess) / 2)
        __ can_place_flags(peaks, current_guess
            lower_guess _ current_guess
        ____
            upper_guess _ current_guess

    r_ lower_guess


___ can_place_flags(peaks, flags_to_place
    current_position _ 1 - flags_to_place
    ___ i __ range(flags_to_place
        __ current_position + flags_to_place > l..(peaks) - 1:
            r_ False
        current_position _ peaks[current_position + flags_to_place]
    r_ current_position < l..(peaks)

test_trail _ [1,5,3,4,3,4,1,2,3,4,6,2]
print(solution(test_trail))

