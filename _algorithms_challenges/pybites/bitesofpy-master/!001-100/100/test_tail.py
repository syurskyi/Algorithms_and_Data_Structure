import pytest

from Previous.tail import tail

content = b"""Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


# https://docs.pytest.org/en/latest/tmpdir.html#the-tmpdir-factory-fixture

@pytest.fixture
def my_file(tmp_path):
    f = tmp_path / "some_file.txt"
    f.write_bytes(content)
    return f


def test_tail_various_args(my_file):
    assert tail(my_file.resolve(), 1) == ['Become a PyBites ninja!']
    assert tail(my_file.resolve(), 2) == ['Keep calm and code in Python!',
                                          'Become a PyBites ninja!']


def test_tail_arg_gt_num_lines_files(my_file):
    # n of > file length basically gets the whole file, but need to do some
    # byte to str conversion and strip off last line's newline char
    actual = tail(my_file.resolve(), 10)
    expected = [line.decode("utf-8")
                for line in content.splitlines()]
    assert actual == expected