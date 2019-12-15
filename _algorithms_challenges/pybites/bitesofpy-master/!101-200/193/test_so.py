import pytest
from so import top_python_questions

actual_return = top_python_questions()
expected_return = [
    ('What does the “yield” keyword do?', 9169),
    ('Does Python have a ternary conditional operator?', 5135),
    ('What does if __name__ == “__main__”: do?', 4927),
    ('Calling an external command in Python', 4190),
    ('How to merge two dictionaries in a single expression?', 3874),
    ('How do I sort a dictionary by value?', 3394),
    ('Using global variables in a function', 2768),
    ('Understanding slice notation', 2707),
    ('How to make a flat list out of list of lists', 2545),
    ('How do I install pip on Windows?', 2388),
    ('How do I pass a variable by reference?', 2295),
    ('How to clone or copy a list?', 2063),
    ('How to read a file line-by-line into a list?', 2000),
    ('Converting string into datetime', 1816),
    ('How to print without newline or space?', 1615),
    ('Select rows from a DataFrame based on '
     'values in a column in pandas', 1304),
    ("Why does comparing strings using either '==' or 'is' "
     'sometimes produce a different result?', 1008)
]


@pytest.mark.parametrize('actual, expected',
                         zip(actual_return, expected_return)
                         )
def test_top_python_questions(actual, expected):
    assert actual == expected