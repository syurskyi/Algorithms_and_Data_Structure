# This is the solution for CountingElements > MaxCounters
#
# This is marked as RESPECTABLE difficulty

___ solution(N, A
    counters _ [0] * N
    start_line _ 0
    current_max _ 0
    ___ i __ A:
        x _ i - 1
        __ i > N:
            start_line _ current_max
        elif counters[x] < start_line:
            counters[x] _ start_line + 1
        ____
            counters[x] +_ 1
        __ i <_ N and counters[x] > current_max:
            current_max _ counters[x]
    ___ i __ range(0, len(counters)):
        __ counters[i] < start_line:
            counters[i] _ start_line
    r_ counters

print (solution(5, [3, 4, 4, 6, 1, 4, 4]))
