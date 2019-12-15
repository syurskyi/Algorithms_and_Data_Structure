from list_comprehensions import filter_positive_even_numbers


def test_filter_positive_and_negatives():
    numbers = list(range(-10, 11))
    assert filter_positive_even_numbers(numbers) == [2, 4, 6, 8, 10]


def test_only_positives():
    numbers = [2, 4, 51, 44, 47, 10]
    assert filter_positive_even_numbers(numbers) == [2, 4, 44, 10]


def test_filter_zero_and_negatives():
    numbers = [0, -1, -3, -5]
    assert filter_positive_even_numbers(numbers) == []