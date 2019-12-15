import sys
import unicodedata

START_EMOJI_RANGE = 100000  # estimate


def what_means_emoji(emoji):
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    try:
        return unicodedata.name(emoji)
    except TypeError:
        return 'Not found'


def _make_emoji_mapping():
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""
    if _make_emoji_mapping.MAPPING:
        res = _make_emoji_mapping.MAPPING
    else:
        res = dict()
        for em in range(START_EMOJI_RANGE, sys.maxunicode + 1):
            emoji = chr(em)
            try:
                desc = what_means_emoji(emoji)
                if desc != 'Not found':
                    res[emoji] = desc.lower()
            except ValueError:
                pass
        _make_emoji_mapping.MAPPING = res
    return res


_make_emoji_mapping.MAPPING = None


def find_emoji(term):
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""
    term = term.lower()
    emoji_mapping = _make_emoji_mapping()
    for em, desc in emoji_mapping.items():
        if term in desc:
            print(f'{desc:40} | {em}')
