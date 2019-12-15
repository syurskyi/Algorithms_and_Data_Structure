from unicodedata import decomposition


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return [c for c in text.lower() if decomposition(c) != '']
