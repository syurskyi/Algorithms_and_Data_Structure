import pytest

from Previous.indents import count_indents


@pytest.mark.parametrize("input_string, count", [
   ('string  ', 0),
   ('  string', 2),
   ('    string', 4),
   ('            string', 12),
])
def test_count_indents(input_string, count):
    assert count_indents(input_string) == count