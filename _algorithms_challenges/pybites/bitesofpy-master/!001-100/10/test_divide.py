import pytest

from divide import positive_divide


def test_positive_divide_good_values():
    assert positive_divide(1, 2) == 0.5
    assert positive_divide(1, 0) == 0
    assert positive_divide(-1, -2) == 0.5
    assert positive_divide(1.5, 2) == 0.75


def test_positive_divide_exceptions():
    try:
        positive_divide(2, 0)
    except ZeroDivisionError:
        pytest.fail("Unexpected ZeroDivisionError!")
    with pytest.raises(TypeError):
        positive_divide(1, 's')
        positive_divide([], 2)
    with pytest.raises(ValueError):
        positive_divide(1, -2)
        positive_divide(-1, 2)