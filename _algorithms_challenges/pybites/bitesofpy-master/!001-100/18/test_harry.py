from harry import get_harry_most_common_word


def test_get_harry_most_common_word():
    top_word = get_harry_most_common_word()
    assert type(top_word) == tuple
    assert top_word[0] == 'dursley'
    assert top_word[1] == 45