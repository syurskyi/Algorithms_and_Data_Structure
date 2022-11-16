# This is the solution for Dynamic programming > NumberSolitaire
#
# This is marked as RESPECTABLE difficulty
# Note here we have the evolution of the algorithm. Only the last function is the correct one.

___ solutionRecursive(A
    r_ max_sum_six_distances(A, 0)


___ max_sum_six_distances(a, position
    __ position __ l..(a) - 1:
        r_ a[position]
    ____
        max_forward _ min(l..(a) - position, 6)
        current_max _ -100000
        ___ i __ range(1, max_forward
            local_max _ max_sum_six_distances(a, position + i)
            current_max _ max(current_max, local_max)
        r_ current_max + a[position]


___ solutionMemoize(A
    values _ [-100000] * l..(A)
    r_ max_sum_six_distancesMem(A, 0, values)


___ max_sum_six_distancesMem(a, position, values
    __ position __ l..(a) - 1:
        r_ a[position]
    __ values[position] __ -100000:
        max_forward _ min(l..(a) - position, 6)
        current_max _ -100000
        ___ i __ range(1, max_forward
            local_max _ max_sum_six_distancesMem(a, position + i, values)
            current_max _ max(current_max, local_max)
        values[position] _ current_max + a[position]
    r_ values[position]


___ solution(A
    values _ [0] * l..(A)
    values[l..(A) - 1] _ A[l..(A) - 1]
    ___ i __ range(l..(A) - 2, -1, -1
        values[i] _ A[i] + find_max_between(values, i + 1, 6)
    r_ values[0]


___ find_max_between(values, start, length
    max _ values[start]
    upto _ min(start + length, l..(values))
    ___ i __ range(start, upto
        __ values[i] > max:
            max _ values[i]
    r_ max


print(solutionRecursive([1, -2, 0, 9, -1, -2, 5, -4]))
print(solutionRecursive([1, -2, 0, 9, -1, -2, 5, -4, -5, -1, -10, -5, -6, -4, -2]))

print(solutionMemoize([1, -2, 0, 9, -1, -2, 5, -4]))
print(solutionMemoize([1, -2, 0, 9, -1, -2, 5, -4, -5, -1, -10, -5, -6, -4, -2]))

print(solution([1, -2, 0, 9, -1, -2, 5, -4]))
print(solution([1, -2, 0, 9, -1, -2, 5, -4, -5, -1, -10, -5, -6, -4, -2]))
