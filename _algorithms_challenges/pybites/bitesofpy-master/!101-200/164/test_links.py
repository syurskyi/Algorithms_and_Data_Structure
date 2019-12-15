from os import path
import platform
import subprocess

import pytest

# no need to import make_html_links as we call links.py from CLI!

TMP = '/tmp'
SCRIPT = 'links.py'
IS_LOCAL = platform.system() in ['Darwin', 'Linux']
MY_CODE = SCRIPT if IS_LOCAL else path.join(TMP, SCRIPT)


# https://docs.pytest.org/en/latest/tmpdir.html#the-tmpdir-factory-fixture

@pytest.fixture
def my_file(tmp_path):
    f = tmp_path / "some_file.txt"
    return f


def _create_and_verify_links(my_file, lines, expected_links):
    my_file.write_bytes(b'\n'.join(lines))
    cmd = f'cat {my_file.resolve()} | python {MY_CODE}'
    output = subprocess.check_output(cmd, shell=True).splitlines()
    assert all(link in output for link in expected_links)


def test_make_html_links_first_data_set(my_file):
    lines = [b"https://www.python.org, Python Homepage",
             b"bad data,blabla,123",
             (b"https://pybit.es/generators.html , "
              b"Generators are Awesome "),
             b"more bad data"]

    expected_links = [(b'<a href="https://www.python.org" target="_blank">'
                       b'Python Homepage</a>'),
                      (b'<a href="https://pybit.es/generators.html">'
                       b'Generators are Awesome</a>')]

    _create_and_verify_links(my_file, lines, expected_links)


def test_make_html_links_second_data_set(my_file):
    lines = [b"bogus data, again",
             b"https://codechalleng.es/bites/ , Bites of Py",
             (b"https://stackoverflow.com/a/12927564,How to capture"
              b" subprocess.call stdout"),
             b"https://pybit.es/,Our labor of love",
             b"https://pybit.es/pages/about.html, About Us",
             b"https://nu.nl, Dutch news site",
             b"And some more bad data !!"]

    expected_links = [(b'<a href="https://codechalleng.es/bites/">'
                       b'Bites of Py</a>'),
                      (b'<a href="https://stackoverflow.com/a/12927564" '
                       b'target="_blank">How to capture subprocess.call '
                       b'stdout</a>'),
                      b'<a href="https://pybit.es/">Our labor of love</a>',
                      (b'<a href="https://pybit.es/pages/about.html">'
                       b'About Us</a>'),
                      (b'<a href="https://nu.nl" target="_blank">'
                       b'Dutch news site</a>')]

    _create_and_verify_links(my_file, lines, expected_links)