from itertools import combinations


def find_number_pairs(numbers, N=10):
    return [n for n in combinations(numbers, 2) if sum(n) == N]
