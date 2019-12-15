import pytest

from fill import prefill_with_character, HTML_SPACE

DIFF_FILL = 'x'


@pytest.mark.parametrize("value, len_, fill, result", [
    (1, 4, HTML_SPACE, f'{HTML_SPACE*3}1'),
    (20, 4, HTML_SPACE, f'{HTML_SPACE*2}20'),
    (315, 4, HTML_SPACE, f'{HTML_SPACE}315'),
    (1239, 4, HTML_SPACE, '1239'),
    (8, 5, DIFF_FILL, f'{DIFF_FILL*4}8'),
    (12, 5, DIFF_FILL, f'{DIFF_FILL*3}12'),
    (139, 5, DIFF_FILL, f'{DIFF_FILL*2}139'),
    (9827, 5, DIFF_FILL, f'{DIFF_FILL}9827'),
    (12345, 5, DIFF_FILL, '12345'),
])
def test_prefill_with_character(value, len_, fill, result):
    assert prefill_with_character(value, column_length=len_,
                                    fill_char=fill) == result