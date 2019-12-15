import pytest

from Previous.dt_convert import years_ago, convert_eu_to_us_date


def test_years_ago():
    assert years_ago('8 Aug, 2015') == 3
    assert years_ago('6 Sep, 2014') == 4
    assert years_ago('1 Oct, 2010') == 8
    assert years_ago('31 Dec, 1958') == 60


def test_years_ago_wrong_input():
    with pytest.raises(ValueError):
        # Sept != valid %b value 'Sep'
        assert years_ago('6 Sept, 2014') == 4


def test_convert_eu_to_us_date():
    assert convert_eu_to_us_date('11/03/2002') == '03/11/2002'
    assert convert_eu_to_us_date('18/04/2008') == '04/18/2008'
    assert convert_eu_to_us_date('12/12/2014') == '12/12/2014'
    assert convert_eu_to_us_date('1/3/2004') == '03/01/2004'


def test_convert_eu_to_us_date_invalid_day():
    with pytest.raises(ValueError):
        convert_eu_to_us_date('41/03/2002')


def test_convert_eu_to_us_date_invalid_month():
    with pytest.raises(ValueError):
        convert_eu_to_us_date('11/13/2002')


def test_convert_eu_to_us_date_invalid_year():
    with pytest.raises(ValueError):
        convert_eu_to_us_date('11/13/year')