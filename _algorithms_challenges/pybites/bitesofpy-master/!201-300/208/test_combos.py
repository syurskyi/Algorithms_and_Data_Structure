import pytest

from Previous.combos import find_number_pairs


def _sort_all(ret):
    return sorted(
        [tuple(sorted(n)) for n in ret]
    )


@pytest.mark.parametrize("numbers, N, expected", [
    ([2, 3, 5, 4, 6], 10, [(4, 6)]),
    ([9, 1, 3, 8, 7], 10, [(9, 1), (3, 7)]),
    ([0.2, 3, 0.4], 10, []),
    ([0.2, 9.8, 10, 1, 0], 10, [(0.2, 9.8), (10, 0)]),
    ([0.24, 0.36, 0.04, 0.06, 0.33, 0.08, 0.20, 0.27, 0.3, 0.31,
      0.76, 0.05, 0.08, 0.08, 0.67, 0.09, 0.66, 0.79, 0.95], 1,
     [(0.24, 0.76), (0.33, 0.67), (0.05, 0.95)]),
    ([9, 1, 3, 8, 7], 0, []),
    ([-9, 29, 11, 10, 9, 3, -1, 21], 20, [(-9, 29), (11, 9), (-1, 21)]),
    ([1.69, 1.82, 2.91, 4.67, 4.81, 3.05, 5.82, 5.06,
      4.28, 6.36, 5.19, 4.57], 10, [(4.81, 5.19)]),
])
def test_find_number_pairs(numbers, N, expected):
    actual = find_number_pairs(numbers, N=N)
    assert type(actual) == list
    assert _sort_all(actual) == _sort_all(expected)