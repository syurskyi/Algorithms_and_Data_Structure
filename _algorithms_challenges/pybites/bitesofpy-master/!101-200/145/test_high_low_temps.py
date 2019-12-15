import datetime

import pytest

from Previous.high_low_temps import STATION
from Previous.high_low_temps import high_low_record_breakers_for_2015 as hl_2015


@pytest.fixture(scope="module")
def high_low():
    return hl_2015()


def test_for_correct_return_of_hl_2015(high_low):
    assert len(high_low) == 2
    assert isinstance(high_low[0], STATION)
    assert isinstance(high_low[1], STATION)


def test_high_hl_2015(high_low):
    high = high_low[0]
    assert high.ID == "USW00014853"
    assert high.Date == datetime.date(2015, 7, 29)
    assert high.Value == 36.1


def test_low_hl_2015(high_low):
    low = high_low[1]
    assert low.ID == "USW00094889"
    assert low.Date == datetime.date(2015, 2, 20)
    assert low.Value == -34.3