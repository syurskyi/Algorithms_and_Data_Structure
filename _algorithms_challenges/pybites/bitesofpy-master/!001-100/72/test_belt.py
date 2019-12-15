import pytest

from Previous.belt import get_belt


@pytest.mark.parametrize("input_argument, expected_return", [
    (0, None),
    (9, None),
    (10, 'white'),
    (48, 'white'),
    (50, 'yellow'),
    (101, 'orange'),
    (249, 'green'),
    (250, 'blue'),
    (251, 'blue'),
    (400, 'brown'),
    (599, 'brown'),
    (600, 'black'),
    (788, 'black'),
    (800, 'paneled'),
    (999, 'paneled'),
    (1000, 'red'),
    (1200, 'red'),
])
def test_get_belt(input_argument, expected_return):
    assert get_belt(input_argument) == expected_return