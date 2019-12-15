from datetime import timedelta

import pytest

from humanize_date import pretty_date, NOW


def n_days_ago_str(days):
    return (NOW - timedelta(days=days)).strftime('%m/%d/%y')


@pytest.mark.parametrize("arg, expected", [
    (NOW - timedelta(seconds=2), 'just now'),
    (NOW - timedelta(seconds=9), 'just now'),
    (NOW - timedelta(seconds=10), '10 seconds ago'),
    (NOW - timedelta(seconds=59), '59 seconds ago'),
    (NOW - timedelta(minutes=1), 'a minute ago'),
    (NOW - timedelta(minutes=1, seconds=40), 'a minute ago'),
    (NOW - timedelta(minutes=2), '2 minutes ago'),
    (NOW - timedelta(minutes=59), '59 minutes ago'),
    (NOW - timedelta(hours=1), 'an hour ago'),
    (NOW - timedelta(hours=2), '2 hours ago'),
    (NOW - timedelta(hours=23), '23 hours ago'),
    (NOW - timedelta(hours=24), 'yesterday'),
    (NOW - timedelta(hours=47), 'yesterday'),
    (NOW - timedelta(days=1), 'yesterday'),
    (NOW - timedelta(days=2), n_days_ago_str(2)),
    (NOW - timedelta(days=7), n_days_ago_str(7)),
    (NOW - timedelta(days=100), n_days_ago_str(100)),
    (NOW - timedelta(days=365), n_days_ago_str(365)),
])
def test_pretty_date(arg, expected):
    assert pretty_date(arg) == expected


def test_input_variable_of_wrong_type():
    with pytest.raises(ValueError):
        pretty_date(123)


def test_input_variable_future_date():
    with pytest.raises(ValueError):
        pretty_date(NOW + timedelta(days=1))