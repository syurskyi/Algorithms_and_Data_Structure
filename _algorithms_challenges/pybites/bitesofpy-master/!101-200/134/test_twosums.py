import pytest
from random import sample, seed

from twosums import two_sums

NUMBERS = [
    2202, 9326, 1034, 4180, 1932, 8118, 7365, 7738, 6220, 3440, 1538, 7994, 465, 
    6387, 7091, 9953, 35, 7298, 4364, 3749, 9686, 1675, 5201, 502, 366, 417, 
    8871, 151, 6246, 3549, 6916, 476, 8645, 3633, 7175, 8124, 9059, 3819, 5664, 
    3783, 3585, 7531, 4748, 353, 6819, 9117, 1639, 3046, 4857, 1981]


def test_two_sums():
    """Test of the example given in the description"""
    numbers = [3, 10, 14, 8, 15, 5, 16, 13, 9, 2]
    expected = (2, 6)
    target = 30
    result = two_sums(numbers, target)
    assert result == expected


@pytest.mark.parametrize("target, expected", [
    (10093, (2, 36)),
    (7067, (27, 30)),
    (11261, (0, 36)),
    (11350, (37, 41)),
    (5224, (31, 42)),
    (2934785974, None),
])
def test_two_sums_param(target, expected):
    result = two_sums(NUMBERS, target)
    assert result == expected


def test_two_sums_random():
    seed(1)
    numbers = sample(range(1, 1_000_000), 1_000)
    picked = sample(numbers, 2)
    index1 = numbers.index(picked[0])
    index2 = numbers.index(picked[1])
    ordered = sorted([index1, index2])
    expected = ordered[0], ordered[1]
    target = sum(picked)
    result = two_sums(numbers, target)
    assert result == expected


def test_two_sums_none():
    result = two_sums(NUMBERS, 7000)
    assert result is None