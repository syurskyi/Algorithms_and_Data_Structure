from datetime import datetime

from Previous.timezone import what_time_lives_pybites


def test_what_time_lives_pybites_spanish_summertime():
    # AUS is 8 hours ahead of ES
    naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)
    aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)

    assert aus_dt.year == 2018
    assert aus_dt.month == 4
    assert aus_dt.day == 28
    assert aus_dt.hour == 8
    assert aus_dt.minute == 55

    assert es_dt.year == 2018
    assert es_dt.month == 4
    assert es_dt.day == 28
    assert es_dt.hour == 0
    assert es_dt.minute == 55


def test_what_time_lives_pybites_spanish_wintertime():
    # AUS is 10 hours ahead of ES
    naive_utc_dt = datetime(2018, 11, 1, 14, 10, 0)
    aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)

    assert aus_dt.year == 2018
    assert aus_dt.month == 11
    assert aus_dt.day == 2
    assert aus_dt.hour == 1
    assert aus_dt.minute == 10

    assert es_dt.year == 2018
    assert es_dt.month == 11
    assert es_dt.day == 1
    assert es_dt.hour == 15
    assert es_dt.minute == 10