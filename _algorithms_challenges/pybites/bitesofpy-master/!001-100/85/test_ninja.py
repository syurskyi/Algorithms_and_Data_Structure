import pytest

from ninja import NinjaBelt

CONGRATS_MSG = ('Congrats, you earned {score} points '
                'obtaining the PyBites Ninja {rank} Belt')
NEW_SCORE_MSG = 'Set new score to {score}'


@pytest.fixture(scope="module")
def ninja():
    """Make a module scope ninja object (save state
       between tests)"""
    return NinjaBelt()


def test_initial_state(ninja):
    assert ninja.score == 0
    assert ninja._last_earned_belt is None


def test_add_score_new_belt(ninja, capfd):
    ninja.score = 20
    output = capfd.readouterr()[0].split('\n')
    assert CONGRATS_MSG.format(score=20, rank='White') in output


def test_add_score_no_new_belt(ninja, capfd):
    ninja.score = 49
    output = capfd.readouterr()[0].split('\n')
    assert NEW_SCORE_MSG.format(score=49) in output


def test_new_score_validation(ninja):
    with pytest.raises(ValueError):
        ninja.score = 'a'
        ninja.score = 40


def test_add_score_another_new_belt(ninja, capfd):
    ninja.score = 50
    output = capfd.readouterr()[0].split('\n')
    assert CONGRATS_MSG.format(score=50, rank='Yellow') in output


def test_add_score_go_two_belts_up(ninja, capfd):
    ninja.score = 177
    output = capfd.readouterr()[0].split('\n')
    assert CONGRATS_MSG.format(score=177, rank='Green') in output
    assert ninja._last_earned_belt.lower() == 'green'