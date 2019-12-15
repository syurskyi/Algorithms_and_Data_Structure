from datetime import datetime
from itertools import compress
import inspect
import re

import pytest

from count_down import count_down

DEFAULT_EXPECTED_OUTPUT = '1234\n123\n12\n1\n'


def test_code_uses_singledispatch_decorator():
    assert '@singledispatch' in inspect.getsource(count_down)


@pytest.mark.parametrize("input_argument", [
    '1234',
    1234,
    [1, 2, 3, 4],
    ['1', '2', '3', '4'],
    (1, 2, 3, 4),
    ('1', '2', '3', '4'),
    {1: 'one', 2: 'two', 3: 'three', 4: 'four'},
    {'1': 'one', '2': 'two', '3': 'three', '4': 'four'},
    range(1, 5),
    {x for x in range(1, 5)},
])
def test_count_down_good_inputs(input_argument, capfd):
    count_down(input_argument)
    output = capfd.readouterr()[0]
    assert output == DEFAULT_EXPECTED_OUTPUT


@pytest.mark.parametrize("input_argument", [
    compress([1, 2, 3, 4], [1, 1, 1, 1]),
    datetime(2018, 4, 21),
    re.compile(r'\d{4}'),
])
def test_count_down_bad_inputs(input_argument, capfd):
    with pytest.raises(ValueError):
        count_down(input_argument)


def test_count_down_float(capfd):
    expected = '12.34\n12.3\n12.\n12\n1\n'
    number = 12.34
    count_down(number)
    output = capfd.readouterr()[0]
    assert output == expected