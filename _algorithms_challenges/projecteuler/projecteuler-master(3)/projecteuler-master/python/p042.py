#!/usr/bin/env python

"""Problem 42: Coded triangle numbers"""

import string
from math import sqrt

from utils import get_path


def main():
    words = get_path('data', 'words.txt').read_text().split('","')
    words[0] = words[0][1:]
    words[-1] = words[-1][:-1]

    char_map = {c: i for i, c in enumerate(string.ascii_uppercase, 1)}
    values = [sum([char_map[char] for char in word]) for word in words]

    triangle_numbers = set([n*(n+1)//2 for n in
                           range(1, (-1 + int(sqrt(1 + 8*max(values))))//2 + 1)])
    return len([v for v in values if v in triangle_numbers])


if __name__ == '__main__':
    print(main())
