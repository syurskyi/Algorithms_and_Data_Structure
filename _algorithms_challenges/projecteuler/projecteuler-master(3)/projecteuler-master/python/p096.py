#!/usr/bin/env python

"""Problem 96: Su Doku"""

from itertools import chain, repeat

from utils import get_path

numbers = set("123456789")
squares = [(row, col) for row in range(9) for col in range(9)]
peers = {}
units = {}

for row, col in squares:
    # Every square has 3 units and 20 peers
    peers[(row, col)] = set(chain(
        [(row, c) for c in range(9) if c != col],
        [(r, col) for r in range(9) if r != row],
        [(r, c) for r in range(row//3*3, row//3*3+3)
         for c in range(col//3*3, col//3*3+3) if r != row or c != col]))

    units[(row, col)] = (
        [(row, c) for c in range(9)],
        [(r, col) for r in range(9)],
        [(r, c) for r in range(row//3*3, row//3*3+3)
         for c in range(col//3*3, col//3*3+3)])


def eliminate(candidates, val, row, col):
    """Eliminate val from a square; propagate when values or places <= 1.
    Return values, except return False if a contradiction is detected."""
    if val not in candidates[row][col]:
        return candidates

    candidates[row][col].remove(val)

    if len(candidates[row][col]) == 0:
        return False  # contradiction: removed last value

    if len(candidates[row][col]) == 1:
        # no easy way to get a value from a set w/o removing it
        for v in candidates[row][col]:
            if not all(eliminate(candidates, v, r, c)
                       for r, c in peers[(row, col)]):
                return False

    for u in units[(row, col)]:
        places = [(r, c) for r, c in u if val in candidates[r][c]]

        if len(places) == 0:
            return False  # contradiction: no place for this value

        if len(places) == 1:
            if not assign(candidates, val, *places[0]):
                return False
    return candidates


def assign(candidates, val, row, col):
    """Eliminate all the other values (except val) from the square's candidates
    and propagate. Return values, except return False if a contradiction is
    detected."""
    other_values = candidates[row][col] - {val}

    if all(eliminate(candidates, v, row, col) for v in other_values):
        return candidates
    return False


def search(candidates):
    """Using depth-first search and propagation, try all possible candidates"""

    if candidates is False:
        return False  # failed earlier

    if all(len(x) == 1 for row in candidates for x in row):
        return candidates  # solved

    # choose an unfilled square with the fewest possibilities
    row, col = min([(r, c) for r, c in squares if len(candidates[r][c]) > 1],
                   key=lambda rc: len(candidates[rc[0]][rc[1]]))

    return first(
        search(
            # create a new copy of the grid for each recursive call to search
            assign([[c.copy() for c in r] for r in candidates], val, row, col))
        for val in candidates[row][col])


def first(seq):
    """Return the first element of seq that is true"""
    return next(filter(None, seq), False)


def solve_puzzle(grid):
    """Solve the puzzle and return the 3-digit number found in the top left
    corner of the solution grid"""
    candidates = [[numbers.copy() for _ in repeat(None, 9)] for _ in repeat(None, 9)]

    for row, col in squares:
        if grid[row][col] != "0":
            assign(candidates, grid[row][col], row, col)

    candidates = search(candidates)

    return int("".join(chain(*candidates[0][:3])))


def main():
    nsum = 0

    with get_path("data", "sudoku.txt").open() as data_file:
        grid = []

        for i, line in enumerate(data_file):
            if i % 10:
                grid.append(line.rstrip())

                if len(grid) == 9:
                    nsum += solve_puzzle(grid)
                    grid *= 0
    return nsum


if __name__ == "__main__":
    print(main())
