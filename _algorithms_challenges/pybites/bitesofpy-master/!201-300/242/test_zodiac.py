from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from zodiac import (get_signs, get_sign_with_most_famous_people,
                    signs_are_mutually_compatible, get_sign_by_date, Sign)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope='module')
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)


# write your pytest code here ...
def test_named_tuple(signs):
    assert list(Sign._fields) == list('name compatibility famous_people sun_dates'.split(' '))
    assert repr(signs[0]).startswith('Sign(')


def test_get_signs(signs):
    assert len(signs) == 12


def test_get_sign_with_most_famouse_people(signs):
    assert get_sign_with_most_famous_people(signs) == ('Scorpio', 35)


@pytest.mark.parametrize("sgn1, sgn2, result", [
    ('Aries', 'Aries', False),
    ('Aries', 'Leo', True),
    ('Aries', 'Capricorn', False),
    ('Aries', 'Aquarius', True)
])
def test_signs_are_mutually_compatible(signs, sgn1, sgn2, result):
    assert signs_are_mutually_compatible(signs, sgn1, sgn2) == result


@pytest.mark.parametrize("dt, result", [
    ([3, 21], 'Aries'),
    ([4, 19], 'Aries'),
    ([4, 20], 'Taurus'),
    ([5, 20], 'Taurus'),
    ([5, 21], 'Gemini'),
    ([6, 20], 'Gemini'),
    ([6, 21], 'Cancer'),
    ([7, 22], 'Cancer'),
    ([7, 23], 'Leo'),
    ([8, 22], 'Leo'),
    ([8, 23], 'Virgo'),
    ([9, 22], 'Virgo'),
    ([9, 23], 'Libra'),
    ([10, 22], 'Libra'),
    ([10, 23], 'Scorpio'),
    ([11, 21], 'Scorpio'),
    ([11, 22], 'Sagittarius'),
    ([12, 21], 'Sagittarius'),
    ([12, 22], 'Capricorn'),  # should be 'Capricorn' but there's a bug in the code!!
    ([1, 19], 'Capricorn'),  # should be 'Capricorn' but there's a bug in the code!!
    ([1, 20], 'Aquarius'),
    ([2, 18], 'Aquarius'),
    ([2, 19], 'Pisces'),
    ([3, 20], 'Pisces')
])
def test_get_sign_by_date(signs, dt, result):
    m, d = dt
    assert get_sign_by_date(signs, datetime(year=2000, month=m, day=d)) == result
