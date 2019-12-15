#!/usr/bin/env python

"""Problem 98: Anagramic squares"""

from collections import defaultdict
from itertools import combinations
from math import ceil, sqrt

from utils import get_path


def main():
    words = get_path('data', 'words.txt').read_text().split('","')
    words[0] = words[0][1:]
    words[-1] = words[-1][:-1]

    tmp = defaultdict(list)

    for word in words:
        tmp[''.join(sorted(word))].append(word)

    anagrams = defaultdict(list)
    for k, v in tmp.items():
        if len(v) > 1:
            anagrams[len(k)].append(v)

    max_square = 0

    for length in sorted(anagrams, reverse=True):

        squares = {str(i*i) for i in range(ceil(sqrt(10**(length-1))),
                                           ceil(sqrt(10**length)))}
        for words in anagrams[length]:
            for first, second in combinations(words, 2):
                chars = len(set(first))

                for square in squares:
                    if len(set(square)) != chars:
                        continue

                    mapping = {}
                    for i, c in enumerate(first):
                        if c in mapping:
                            if c != mapping[c]:
                                break
                        else:
                            mapping[c] = square[i]
                    else:
                        other = "".join([mapping[x] for x in second])
                        if other in squares:
                            max_square = max(max_square, int(square), int(other))
        if max_square:
            return max_square


if __name__ == '__main__':
    print(main())
