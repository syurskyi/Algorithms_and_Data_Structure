import string

import pytest

from spelling import suggest_word, load_words


@pytest.fixture(scope='module')
def a_words():
    """Get only a[abcdefghijklm]-words to speed up tests"""
    words = load_words()
    return {word for word in words
            if word.startswith('a') and len(word) > 1
            and word[1] in string.ascii_letters[:13]}


@pytest.mark.parametrize("word, expected", [
    ('acheive', 'achieve'),
    ('accross', 'across'),
    ('acceptible', 'acceptable'),
    ('allmost', 'almost'),
    ('aquire', 'acquire'),
    ('agressive', 'aggressive'),
    ('accomodate', 'accommodate'),
    ('accidentaly', 'accidentally'),
])
def test_suggest_word(word, expected, a_words):
    assert suggest_word(word, words=a_words) == expected