import pytest

from Previous.animation import spinner, SPINNER_STATES as states


@pytest.mark.parametrize("seconds, rounds, slice_", [
    (0.2, 0, 2),
    (0.4, 1, 0),
    (1, 2, 2),
    (1.2, 3, 0),
])
def test_spinner(monkeypatch, capfd, seconds, rounds, slice_):
    spinner(seconds)
    actual = capfd.readouterr()[0].strip().split('\r')
    expected = states * rounds
    if slice_:
        expected += states[:slice_]
    assert actual == expected