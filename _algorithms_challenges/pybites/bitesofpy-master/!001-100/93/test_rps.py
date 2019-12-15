from unittest.mock import patch

import pytest

from rps import (_get_winner, game,
                 lose, win, tie)


@pytest.fixture()
def my_game():
    """Initialize game and move it to point where to
       receive first player (send) input"""
    gen = game()
    next(gen)
    return gen


@patch('rps._get_computer_move')
def test_win(computerMoveMock, my_game, capfd):
    computerMoveMock.return_value = 'rock'
    my_game.send('paper')
    output = capfd.readouterr()[0].strip()
    assert output == win.format('paper', 'rock')


@patch('rps._get_computer_move')
def test_loose(computerMoveMock, my_game, capfd):
    computerMoveMock.return_value = 'rock'
    my_game.send('scissors')
    output = capfd.readouterr()[0].strip()
    assert output == lose.format('rock', 'scissors')


@patch('rps._get_computer_move')
def test_tie(computerMoveMock, my_game, capfd):
    computerMoveMock.return_value = 'paper'
    my_game.send('paper')
    output = capfd.readouterr()[0].strip()
    assert output == tie


@patch('rps._get_computer_move')
def test_invalid_choice(computerMoveMock, my_game, capfd):
    my_game.send('spam')
    output = capfd.readouterr()[0].strip()
    assert 'Invalid' in output


@pytest.mark.parametrize("player1, player2, result", [
    ('scissors', 'paper', 'lose'),
    ('paper', 'scissors', 'win'),
    ('rock', 'paper', 'win'),
    ('paper', 'rock', 'lose'),
    ('rock', 'scissors', 'lose'),
    ('scissors', 'rock', 'win'),
    ('rock', 'rock', 'tie'),
    ('scissors', 'scissors', 'tie'),
    ('paper', 'paper', 'tie'),
])
def test_get_winner(player1, player2, result):
    assert result in _get_winner(player1, player2)


def test_stop_iteration(my_game):
    # 3.6 = StopIteration
    # 3.7 = RuntimeError - see: https://bugs.python.org/issue32670
    with pytest.raises((StopIteration, RuntimeError)):
        my_game.send('q')