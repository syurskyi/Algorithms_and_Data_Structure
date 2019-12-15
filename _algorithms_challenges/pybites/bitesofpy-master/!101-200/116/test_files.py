import os
from tempfile import TemporaryDirectory

import pytest

from files import get_files

TMP = '/tmp'


@pytest.mark.parametrize("byte_sizes, size_in_kb, expected", [
    ([800, 1000, 1200], 1, ['1200']),
    ([1024, 1025], 1, ['1024', '1025']),
    ([1024, 1025], 1.026, []),
    ([1000, 1300, 1777, 900], 1.25, ['1300', '1777']),
    ([1024, 2047, 2048, 2500], 2, ['2048', '2500']),
])
def test_get_files(byte_sizes, size_in_kb, expected):
    with TemporaryDirectory(dir=TMP) as dirname:
        for size in byte_sizes:
            with open(os.path.join(dirname, str(size)), 'wb') as f:
                f.write(os.urandom(size))

        actual = [os.path.basename(fi) for fi in
                  get_files(dirname, size_in_kb)]
        assert sorted(actual) == sorted(expected)