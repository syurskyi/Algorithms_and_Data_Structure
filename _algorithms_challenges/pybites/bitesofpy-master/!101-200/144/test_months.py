import pytest

from months import calc_months_passed


def test_same_date():
    assert calc_months_passed(2018, 11, 1) == 0


def test_nine_days_later():
    assert calc_months_passed(2018, 11, 10) == 0


def test_ten_days_later():
    assert calc_months_passed(2018, 11, 11) == 1


def test_one_month_and_nine_days_later():
    assert calc_months_passed(2018, 12, 10) == 1


def test_one_month_and_ten_day_later():
    assert calc_months_passed(2018, 12, 11) == 2


def test_one_year_one_month_and_nine_days_later():
    assert calc_months_passed(2019, 12, 10) == 13


def test_one_year_one_month_and_ten_days_later():
    assert calc_months_passed(2019, 12, 11) == 14


def test_non_int_input_args():
    with pytest.raises(TypeError):
        calc_months_passed('a', 10, 1)
    with pytest.raises(TypeError):
        calc_months_passed(2018, 'b', 1)
    with pytest.raises(TypeError):
        calc_months_passed(2018, 10, 'c')


def test_out_of_dt_range_args():
    with pytest.raises(ValueError):
        calc_months_passed(-1000, 11, 1)
    with pytest.raises(ValueError):
        calc_months_passed(2018, 13, 1)
    with pytest.raises(ValueError):
        calc_months_passed(2018, 11, 34)


def test_new_date_in_past_raises_value_error():
    with pytest.raises(ValueError):
        calc_months_passed(2018, 10, 1)