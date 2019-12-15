"""Complete remove_punctuation which receives an input string and strips out all punctuation characters (!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~).

Return the resulting string. You can go full loop, list comprehension or maybe some nice stdlib functionality?"""

from string import punctuation


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    table = str.maketrans({key: None for key in punctuation})
    return input_string.translate(table)
