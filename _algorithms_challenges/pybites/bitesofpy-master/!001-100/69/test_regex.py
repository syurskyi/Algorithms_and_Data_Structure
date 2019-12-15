from regex import (has_timestamp, is_integer,
                   has_word_with_dashes, remove_all_parenthesis_words,
                   split_string_on_punctuation, remove_duplicate_spacing,
                   has_three_consecutive_vowels,
                   convert_emea_date_to_amer_date)


def test_has_timestamp():
    assert has_timestamp('INFO 2014-07-03T23:27:51 Shutdown initiated.')
    assert has_timestamp('INFO 2014-06-01T13:28:51 Shutdown initiated.')
    assert not has_timestamp('INFO 2014-7-3T23:27:51 Shutdown initiated.')
    assert not has_timestamp('INFO 2014-07-03t23:27:1 Shutdown initiated.')


def test_is_integer():
    assert is_integer(1)
    assert is_integer(-1)
    assert not is_integer('str')
    assert not is_integer(1.1)


def test_has_word_with_dashes():
    assert has_word_with_dashes('this Bite is self-contained')
    assert has_word_with_dashes('the match ended in 1-1')
    assert not has_word_with_dashes('this Bite is not selfcontained')
    assert not has_word_with_dashes('the match ended in 1- 1')


def test_remove_all_parenthesis_words():
    input_string = 'good morning (afternoon), how are you?'
    expected = 'good morning, how are you?'
    assert remove_all_parenthesis_words(input_string) == expected
    input_string = 'math (8.6) and science (9.1) where his strengths'
    expected = 'math and science where his strengths'
    assert remove_all_parenthesis_words(input_string) == expected


def test_split_string_on_punctuation():
    input_string = 'hi, how are you doing? blabla'
    expected = ['hi', 'how are you doing', 'blabla']
    assert split_string_on_punctuation(input_string) == expected
    input_string = ';String. with. punctuation characters!'
    expected = ['String', 'with', 'punctuation characters']
    assert split_string_on_punctuation(input_string) == expected


def test_remove_duplicate_spacing():
    input_string = 'This is a   string with  too    much spacing'
    expected = 'This is a string with too much spacing'
    assert remove_duplicate_spacing(input_string) == expected


def test_has_three_consecutive_vowels():
    assert has_three_consecutive_vowels('beautiful')
    assert has_three_consecutive_vowels('queueing')
    assert not has_three_consecutive_vowels('mountain')
    assert not has_three_consecutive_vowels('house')


def test_convert_emea_date_to_amer_date():
    assert convert_emea_date_to_amer_date('31/03/2018') == '03/31/2018'
    assert convert_emea_date_to_amer_date('none') == 'none'