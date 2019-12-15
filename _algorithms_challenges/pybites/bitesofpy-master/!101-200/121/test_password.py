import pytest

from password import password_complexity


@pytest.mark.parametrize("arg, expected", [
    ('abc', 0),
    ('ABC', 0),
    ('123', 0),
    ('abc1', 1),
    ('ABC1', 1),
    ('@', 1),
    ('aA@', 2),
    ('aA1@', 3),
    ('aA1@1224', 4),  # repeated 2
    ('aA1@1234', 5),
    ('aaaabbbbc', 1),
    ('abcdabcd', 2),
    ('Abcdabcd', 3),
    ('Abcdabc$', 4),
    ('Abcdab1$', 5),
    ('Abcdaac$', 3),
    ('123$abc', 2),
    ('123$abC', 3),
    ('123$abcd', 4),
    ('123$abC1', 5),
    ('123$abb1', 3),
    ('123$Abb1', 4),
    ('123$Abc1', 5),
    ('@@@@@@@@@@', 2),
    ('@$@$@$@$@$', 3),
])
def test_password_complexity(arg, expected):
    assert password_complexity(arg) == expected