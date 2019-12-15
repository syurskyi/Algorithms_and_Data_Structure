import inspect

from summing import sum_numbers


def test_functionality():
    numbers = [1, 2, 0, 4, 5, 12, 'a', 3]
    actual = list(sum_numbers(numbers))
    expected = [0.5, 0.0, 0.8, 0.4166666666666667]
    assert actual == expected


def test_use_of_idioms():
    src = inspect.getsource(sum_numbers)
    assert 'try' not in src
    assert 'except ' not in src
    assert 'yield' in src
    assert 'TypeError' in src
    assert 'ZeroDivisionError' in src
    assert src.count('suppress(') in (1, 2)
    assert src.count('with') in (1, 2)