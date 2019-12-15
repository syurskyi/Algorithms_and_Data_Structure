import re

import pytest

from Previous.wc import wc

lines = [b'Hello world',
         b'Keep calm and code in Python',
         b'Have a nice weekend']


@pytest.mark.parametrize("some_text, expected", [
    (lines[0], '1 2 11'),
    (b'\n'.join(lines[:2]), '2 8 40'),
    (b'\n'.join(lines), '3 12 60'),
])
def test_wc(some_text, expected, tmp_path):
    f = tmp_path / "some_file.txt"
    f.write_bytes(some_text)
    output = wc(f.resolve())
    # replace tabs / multiple spaces by single space
    output = re.sub(r'\t|\s+', ' ', output)

    assert expected in output
    # file with/without path allowed
    assert f.name in output