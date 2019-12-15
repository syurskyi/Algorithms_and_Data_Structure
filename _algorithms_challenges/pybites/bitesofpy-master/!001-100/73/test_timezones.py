from datetime import datetime

import pytest

from timezones import within_schedule


def test_too_late_aus():
    # local hours [15, 23, 8]
    dt = datetime(2018, 4, 18, 13, 28)
    timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
    assert not within_schedule(dt, *timezones)


def test_all_good_aus_just_in_time_summertime():
    # local hours [14, 22, 7]
    dt = datetime(2018, 4, 18, 12, 28)
    timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
    assert within_schedule(dt, *timezones)


def test_change_winter_time_aus_now_too_late():
    # local hours [14, 23, 7]
    dt = datetime(2018, 10, 18, 12, 28)
    timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
    assert not within_schedule(dt, *timezones)


def test_too_late_for_chicago():
    # local hours [8, 16, 1]
    dt = datetime(2018, 4, 18, 6, 45)
    timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
    assert not within_schedule(dt, *timezones)


def test_wrong_timezone():
    dt = datetime(2018, 4, 18, 12, 28)
    timezones = ['Europe/Madrid', 'bogus']
    with pytest.raises(ValueError):
        within_schedule(dt, *timezones)