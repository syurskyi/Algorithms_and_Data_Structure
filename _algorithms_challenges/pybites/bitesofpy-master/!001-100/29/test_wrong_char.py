from Previous.wrong_char import get_index_different_char


def test_wrong_char():
    inputs = (
        ['A', 'f', '.', 'Q', 2],
        ['.', '{', ' ^', '%', 'a'],
        [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
        ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
        list(range(1,9)) + ['}'] + list('abcde'),  # noqa E230
        [2, '.', ',', '!']
    )
    expected = [2, 4, 1, 5, 8, 0]

    for arg, exp in zip(inputs, expected):
        err = f'get_index_different_char({arg}) should return index {exp}'
        assert get_index_different_char(arg) == exp, err