import string


def _check(key):
    if key[0] not in string.digits:
        key = f'\1{key}'
    return key.lower()


def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case,
       one twist: numbers have to appear after letters!"""
    return sorted(words, key=_check)
