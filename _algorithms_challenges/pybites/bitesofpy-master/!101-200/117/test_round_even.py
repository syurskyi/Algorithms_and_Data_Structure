import pytest

from round_even import round_even


@pytest.mark.parametrize("arg, expected", [
    (0.4, 0),
    (0.5, 0),  # nearest even int
    (0.6, 1),
    (1.4, 1),
    (1.5, 2),
    (1.6, 2),
    (2.5, 2),  # nearest even int
])
def test_round_even(arg, expected):
    assert round_even(arg) == expected