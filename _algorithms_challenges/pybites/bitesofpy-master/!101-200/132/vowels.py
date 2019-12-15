VOWELS = list('aeiou')


def _count(w: str):
    return len([l for l in w if l in VOWELS])


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    words = [(w, _count(w)) for w in text.split(' ')]
    return sorted(words, key=lambda x: -x[1])[0]
