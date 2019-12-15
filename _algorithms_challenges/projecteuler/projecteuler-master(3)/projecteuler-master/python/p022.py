#!/usr/bin/env python

"""Problem 22: Names scores"""

import string

from utils import get_path


def main():
    names = get_path('data', 'names.txt').read_text().split('","')
    names[0] = names[0][1:]
    names[-1] = names[-1][:-1]
    names.sort()

    values = {c: i for i, c in enumerate(string.ascii_uppercase, 1)}

    return sum([sum([values[c] for c in name]) * pos
                for pos, name in enumerate(names, 1)])


if __name__ == '__main__':
    print(main())
