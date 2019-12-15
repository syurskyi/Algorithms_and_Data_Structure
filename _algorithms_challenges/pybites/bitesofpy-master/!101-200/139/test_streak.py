import datetime

from streak import extract_dates, calculate_streak


def test_extract_dates():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-10 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    assert len(dates) == 8  # one less = deduped 2018-09-18
    assert datetime.date(2018, 9, 18) in dates
    assert datetime.date(2018, 10, 23) in dates
    assert datetime.date(2018, 11, 9) in dates


def test_streak_of_0_days():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-10 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 0


def test_streak_of_1_day_can_still_make_today():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 1


def test_streak_of_1_day_thanks_to_todays_progress():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-12 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-16 | bite       | 4       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 1


def test_streak_of_3_days():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-12 | pcc        | 1       |
    | 2018-11-11 | 100d       | 1       |
    | 2018-11-10 | 100d       | 2       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-16 | bite       | 4       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 3


def test_streak_of_10_days():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-08 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-06 | bite       | 1       |
    | 2018-11-05 | bite       | 4       |
    | 2018-11-04 | bite       | 2       |
    | 2018-11-03 | bite       | 4       |
    | 2018-11-02 | 100d       | 2       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 10


def test_streak_of_almost_10_days_but_gap_so_only_5_days():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-08 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-05 | bite       | 4       |
    | 2018-11-04 | bite       | 2       |
    | 2018-11-03 | bite       | 4       |
    | 2018-11-02 | 100d       | 2       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 5


def test_streak_of_5_days_dates_out_of_order():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-08 | pcc        | 1       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 5