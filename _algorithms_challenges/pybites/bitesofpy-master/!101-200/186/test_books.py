import pytest

from books import get_number_books_read


@pytest.mark.parametrize("goal, date_str, expected", [
    (52, 'Sunday, March 18th, 2019', 12),
    (52, 'Sunday, March 25th, 2019', 13),
    (52, 'April 2nd, 2019', 14),
    (100, 'Sunday, March 18th, 2019', 23),
    (100, 'Sunday, March 25th, 2019', 25),
    (100, '2019-04-02', 26),
    (52, None, 11),
    (100, None, 21),
    (100, '11-20-2019', 90),
    (100, '5/20/2019', 40),
])
def test_get_number_books_read(goal, date_str, expected):
    assert get_number_books_read(goal, date_str) == expected


def test_not_positive_goal_exception():
    with pytest.raises(ValueError):
        get_number_books_read(0)
    with pytest.raises(ValueError):
        get_number_books_read(-1)


def test_past_date_exception():
    with pytest.raises(ValueError):
        get_number_books_read(52, '5-20-2018')