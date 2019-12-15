import pytest

from Previous.scrabble import get_possible_dict_words

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


@pytest.mark.parametrize("draw, expected", [
    ('T, I, I, G, T, T, L', 'gilt'),
    ('O, N, V, R, A, Z, H', 'zonar'),
    ('E, P, A, E, I, O, A', ('apio', 'peai')),
    ('B, R, C, O, O, E, O', 'boce'),
    ('G, A, R, Y, T, E, V', 'garvey'),
])
def test_max_word(draw, expected):
    draw = draw.split(', ')
    words = get_possible_dict_words(draw)
    if len(expected) > 1:
        assert max_word_value(words) in expected
    else:
        assert max_word_value(words) == expected