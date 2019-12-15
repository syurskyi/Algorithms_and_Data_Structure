import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize("good_seq, expected_result", [
    ([0, 2, 4, 8], 248),
    ([1, 0, 2], 102)
])
def test_numbers_to_dec(good_seq, expected_result):
    assert list_to_decimal(good_seq) == expected_result


@pytest.mark.parametrize("bad_seq", [
    [-3, 23],
    [5, 10]
])
def test_numbers_to_dec_ValueError(bad_seq):
    with pytest.raises(ValueError):
        list_to_decimal(bad_seq)


@pytest.mark.parametrize("bad_seq", [
    [3.6, 23, 1],
    [1, '2', 3],
    ['3', '6', None]
])
def test_numbers_to_dec_TypeError(bad_seq):
    with pytest.raises(TypeError):
        list_to_decimal(bad_seq)
