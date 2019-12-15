import pytest

from rounding import round_up_or_down

transactions1 = [2.05, 3.55, 4.50, 10.76, 100.25]
transactions2 = [1.55, 9.17, 5.67, 6.77, 2.33]


@pytest.mark.parametrize("transactions, up_arg, expected", [
    (transactions1, True, [3, 4, 5, 11, 101]),
    (transactions1, False, [2, 3, 4, 10, 100]),
    (transactions2, True, [2, 10, 6, 7, 3]),
    (transactions2, False, [1, 9, 5, 6, 2]),
])
def test_round_up_or_down(transactions, up_arg, expected):
    assert round_up_or_down(transactions, up=up_arg) == expected