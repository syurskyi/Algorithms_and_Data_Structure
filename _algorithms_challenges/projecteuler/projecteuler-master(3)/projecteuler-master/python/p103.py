#!/usr/bin/env python

"""Problem 103: Special subset sums: optimum"""

from itertools import combinations


def is_special_sum_set(s):
    """
    Check if a set (represented as a list) is a special sum set.
    """
    s.sort()

    if any(sum(s[:i]) <= sum(s[-i+1:]) for i in range(2, (len(s) + 3)//2)):
        return False

    for i in range(2, len(s)//2+1):
        sums = set()

        for subset in combinations(s, i):
            st_sum = sum(subset)
            if st_sum in sums:
                return False
            sums.add(st_sum)
    return True


def main():
    candidates = []

    # make an educated guess about limits, based on the problem definition
    for s in combinations(range(30, 47), 6):
        s = [20, *s]

        if is_special_sum_set(s):
            candidates.append(s)

    return ''.join(map(str, min(candidates, key=sum)))


if __name__ == '__main__':
    print(main())
