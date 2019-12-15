import pytest

from Previous.validate import int_args


@int_args
def sum_numbers(*numbers):
    return sum(numbers)


def test_valid_args():
    assert sum_numbers(1, 2, 3) == 6


def test_invalid_type_str():
    with pytest.raises(TypeError):
        sum_numbers(1, 'string', 3)


def test_invalid_type_float():
    with pytest.raises(TypeError):
        sum_numbers(1, 2.1, 3)


def test_negative_number():
    with pytest.raises(ValueError):
        sum_numbers(1, 2, -3)