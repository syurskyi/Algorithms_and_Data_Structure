import pytest

from division import divide_numbers


@pytest.mark.parametrize("numerator, denominator, expected", [
    (1, 2, 0.5),
    (8, 2, 4),
    # strings that look like ints are converted (casted) fine
    ('3', '2', 1.5),
    # floats work too but when casted to int they are rounded down!
    (8.2, 2, 4),
    (1, 2.9, 0.5),
])
def test_divide_numbers_good_inputs(numerator, denominator, expected):
    assert divide_numbers(numerator, denominator) == expected


@pytest.mark.parametrize("numerator, denominator", [
    # ignoring dict/set/list to keep it simple, those would actually
    # throw a TypeError when passed into int()
    (2, 's'),
    ('s', 2),
    ('v', 'w'),
])
def test_divide_numbers_raises_value_error(numerator, denominator):
    with pytest.raises(ValueError):
        divide_numbers(numerator, denominator)


def test_divide_by_zero_does_not_raise_zero_division_exception():
    assert divide_numbers(10, 0) == 0