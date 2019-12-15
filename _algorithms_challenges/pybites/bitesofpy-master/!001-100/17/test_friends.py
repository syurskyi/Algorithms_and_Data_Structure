import pytest

from Previous.friends import friends_teams

friends = 'Bob Dante Julian Martin'.split()


@pytest.mark.parametrize('test_input,expected', [
    (('Bob', 'Dante'), True),
    (('Bob', 'Julian'), True),
    (('Bob', 'Martin'), True),
    (('Dante', 'Julian'), True),
    (('Dante', 'Martin'), True),
    (('Julian', 'Martin'), True),
    # order does not matter
    (('Dante', 'Bob'), False),
    (('Julian', 'Bob'), False),
    (('Martin', 'Bob'), False),
    (('Julian', 'Dante'), False),
    (('Martin', 'Dante'), False),
    (('Martin', 'Julian'), False),
    # not with self
    (('Julian', 'Julian'), False),
])
def test_team_of_two_order_does_not_matter(test_input, expected):
    """First test lists all combos"""
    combos = list(friends_teams(friends, team_size=2, order_does_matter=False))
    assert len(combos) == 6
    if expected:
        assert test_input in combos
    else:
        assert test_input not in combos


@pytest.mark.parametrize('test_input,expected', [
    (('Bob', 'Dante'), True),
    (('Dante', 'Julian'), True),
    (('Dante', 'Martin'), True),
    # order does matter
    (('Dante', 'Bob'), True),
    (('Julian', 'Dante'), True),
    (('Martin', 'Dante'), True),
])
def test_team_of_two_order_does_matter(test_input, expected):
    """From here on just test a subset of combos"""
    combos = list(friends_teams(friends, team_size=2, order_does_matter=True))
    assert len(combos) == 12
    assert test_input in combos


@pytest.mark.parametrize('test_input,expected', [
    (('Bob', 'Dante', 'Julian'), True),
    (('Bob', 'Dante', 'Martin'), True),
    (('Bob', 'Julian', 'Martin'), True),
    (('Dante', 'Julian', 'Martin'), True),
    # order does not matter
    (('Dante', 'Bob', 'Martin'), False),
    (('Julian', 'Martin', 'Dante'), False),
    # no one goes twice
    (('Dante', 'Dante', 'Martin'), False),
])
def test_team_of_three_order_does_not_matter(test_input, expected):
    combos = list(friends_teams(friends, team_size=3, order_does_matter=False))
    assert len(combos) == 4
    if expected:
        assert test_input in combos
    else:
        assert test_input not in combos


@pytest.mark.parametrize('test_input,expected', [
    (('Bob', 'Dante', 'Julian'), True),
    (('Bob', 'Dante', 'Martin'), True),
    (('Bob', 'Julian', 'Martin'), True),
    (('Dante', 'Julian', 'Martin'), True),
    # order does matter
    (('Dante', 'Bob', 'Martin'), True),
    (('Julian', 'Martin', 'Dante'), True),
])
def test_team_of_three_order_does_matter(test_input, expected):
    combos = list(friends_teams(friends, team_size=3, order_does_matter=True))
    assert len(combos) == 24
    assert test_input in combos