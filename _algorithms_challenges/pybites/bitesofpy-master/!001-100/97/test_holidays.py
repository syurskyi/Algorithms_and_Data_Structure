import pytest

from Previous.holidays import get_us_bank_holidays


holidays = get_us_bank_holidays()


@pytest.mark.parametrize("month, holiday", [
    ("01", ["New Year's Day", "Martin Luther King Jr. Day"]),
    ("02", ["Presidents' Day"]),
    ("04", ["Emancipation Day"]),
    ("05", ["Mother's Day", "Memorial Day"]),
    ("06", ["Father's Day"]),
    ("07", ["Independence Day"]),
    ("09", ["Labor Day"]),
    ("10", ["Columbus Day"]),
    ("11", ["Veterans Day", "Thanksgiving", "Day after Thanksgiving"]),
    ("12", ["Christmas Day"]),
])
def test_get_us_bank_holidays(month, holiday):
    assert holidays.get(month) == holiday