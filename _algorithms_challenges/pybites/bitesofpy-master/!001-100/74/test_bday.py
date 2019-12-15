from datetime import date

from Previous.bday import weekday_of_birth_date


def test_leonardo_dicaprio_bday():
    dt = date(1974, 11, 11)
    assert weekday_of_birth_date(dt) == 'Monday'


def test_will_smith_bday():
    dt = date(1968, 9, 25)
    assert weekday_of_birth_date(dt) == 'Wednesday'


def test_robert_downey_bday():
    dt = date(1965, 4, 4)
    assert weekday_of_birth_date(dt) == 'Sunday'