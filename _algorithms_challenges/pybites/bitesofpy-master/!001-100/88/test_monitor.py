from collections import Counter
from datetime import date
from unittest.mock import patch, MagicMock

import pytest

from Previous import monitor
from Previous.monitor import timeit, ALERT_MSG


@pytest.fixture()
def clean_cache():
    """Make sure each test starts with a clean cache dict"""
    monitor.violations = Counter()


@patch('monitor.time', MagicMock(side_effect=[0, 2]))
def test_one_operation_within_time(clean_cache, capfd):
    """1 operation took 2 seconds = ok"""
    with timeit():
        pass
    output = capfd.readouterr()[0]
    assert not output


@patch('monitor.time', MagicMock(side_effect=[0, 2, 0, 3]))
def test_two_operations_one_too_long(clean_cache, capfd):
    """2 operations, 1 took >= 3 seconds = still ok"""
    with timeit():
        pass
    # this one took too long
    with timeit():
        pass
    output = capfd.readouterr()[0]
    assert not output


@patch('monitor.time', MagicMock(side_effect=[0, 2, 0, 3, 0, 4]))
def test_three_operations_two_too_long(clean_cache, capfd):
    """3 operations, 2 took >= 3 seconds = still ok"""
    # Note that each timeit call takes the next 2 elements of side_effect
    # = mocked start/end times in seconds
    with timeit():
        pass
    with timeit():
        pass
    with timeit():
        pass
    output = capfd.readouterr()[0]
    assert not output


@patch('monitor.time', MagicMock(side_effect=[0, 2, 0, 3, 0, 4, 0, 5]))
def test_four_operations_three_took_too_long(clean_cache, capfd):
    """4 operations, 3 tooks >= 3 seconds = NOT ok, prints ALERT"""
    with timeit():
        pass
    with timeit():
        pass
    with timeit():
        pass
    with timeit():
        pass
    output = capfd.readouterr()[0]
    assert output.strip() == ALERT_MSG


@patch('monitor.time', MagicMock(side_effect=[0, 3, 0, 3, 0, 4, 0, 5]))
def test_four_operations_took_too_long_but_on_two_days(clean_cache, capfd):
    """4 tooks >= 3 seconds, but spread over 2 days = ok / no alert"""
    # 2 violations yesterday
    with patch('monitor.get_today', return_value=date(2018, 5, 1)):
        with timeit():
            pass
        with timeit():
            pass
    # 2 violations today
    with patch('monitor.get_today', return_value=date(2018, 5, 2)):
        with timeit():
            pass
        with timeit():
            pass
    output = capfd.readouterr()[0]
    assert not output