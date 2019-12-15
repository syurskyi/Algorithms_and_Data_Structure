import pytest

from workouts import (get_workout_motd,
                      CHILL_OUT, INVALID_DAY)


# About parametrize: https://pybit.es/pytest-coding-100-tests.html
@pytest.mark.parametrize("day, expected", [
    ('Monday', 'Go train Chest+biceps'),
    ('monday', 'Go train Chest+biceps'),
    ('Tuesday', 'Go train Back+triceps'),
    ('TuEsdAy', 'Go train Back+triceps'),
    ('Wednesday', 'Go train Core'),
    ('wednesdaY', 'Go train Core'),
    ('Thursday', 'Go train Legs'),
    ('Friday', 'Go train Shoulders'),
    ('Saturday', CHILL_OUT),
    ('Sunday', CHILL_OUT),
    ('sundAy', CHILL_OUT),
    ('nonsense', INVALID_DAY),
    ('monday2', INVALID_DAY),
])
def test_get_workout_valid_case_insensitive_dict_lookups(day, expected):
    assert get_workout_motd(day) == expected