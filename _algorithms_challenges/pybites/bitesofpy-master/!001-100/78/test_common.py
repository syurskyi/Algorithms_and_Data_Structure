import pytest

from common import common_languages


@pytest.fixture()
def programmers():
    return dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
                tim=['Python', 'Haskell', 'C++', 'JS'],
                sara=['Perl', 'C', 'Java', 'Python', 'JS'],
                paul=['C++', 'JS', 'Python'])


def test_common_languages(programmers):
    expected = ['JS', 'Python']
    actual = common_languages(programmers)
    assert sorted(list(actual)) == expected


def test_adding_programmer_without_js(programmers):
    programmers['sue'] = ['Scala', 'Python']
    expected = ['Python']
    actual = common_languages(programmers)
    assert list(actual) == expected


def test_adding_programmer_without_js_nor_python(programmers):
    programmers['fabio'] = ['PHP']
    expected = []
    actual = common_languages(programmers)
    assert list(actual) == expected


def test_common_languages_adding_new_common_language(programmers):
    programmers['bob'].append('C++')
    programmers['sara'].append('C++')
    expected = ['C++', 'JS', 'Python']
    actual = common_languages(programmers)
    assert sorted(list(actual)) == expected