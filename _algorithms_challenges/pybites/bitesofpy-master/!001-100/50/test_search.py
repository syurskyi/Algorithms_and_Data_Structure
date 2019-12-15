from datetime import datetime, date
from unittest.mock import patch

import pytest

from search import (_convert_struct_time_to_dt, get_feed_entries,
                    filter_entries_by_tag, main, Entry)


class AttrDict(dict):
    """feedparser lets you access dict keys as attributes, hence a bit of
       mocking, got this from https://stackoverflow.com/a/14620633"""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


dt1 = datetime(2018, 2, 18, 19, 52, 0).timetuple()
dt2 = datetime(2017, 1, 6, 11, 0, 0).timetuple()

MOCK_ENTRIES = AttrDict({'entries':
                [AttrDict({'author': 'PyBites',
                           'link':
                           'https://pybit.es/twitter_digest_201808.html',  # noqa E501
                           'published': 'Sun, 18 Feb 2018 20:52:00 +0100',  # noqa E501
                           'published_parsed': dt1,
                           'summary': 'Every weekend we share ...',
                           'tags': [AttrDict({'term': 'twitter'}),
                                    AttrDict({'term': 'Flask'}),
                                    AttrDict({'term': 'Python'}),
                                    AttrDict({'term': 'Regex'})],
                           'title': 'Twitter Digest 2018 Week 08'}),
                 AttrDict({'author': 'Julian',
                           'link': 'https://pybit.es/pyperclip.html',
                           'published': 'Fri, 06 Jan 2017 12:00:00 +0100',  # noqa E501
                           'published_parsed': dt2,
                           'summary': 'Use the Pyperclip module to ...',
                           'tags': [AttrDict({'term': 'python'}),
                                    AttrDict({'term': 'tips'}),
                                    AttrDict({'term': 'tricks'}),
                                    AttrDict({'term': 'code'}),
                                    AttrDict({'term': 'pybites'})],
                           'title': 'Copy and Paste with Pyperclip'})]})


@pytest.mark.parametrize("arg, ret", [
    (datetime(2017, 9, 12, 8, 50, 0).timetuple(),
     date(year=2017, month=9, day=12)),
    (datetime(2017, 9, 8, 14, 30, 0).timetuple(),
     date(year=2017, month=9, day=8)),
    (datetime(2016, 12, 19, 9, 26, 0).timetuple(),
     date(year=2016, month=12, day=19)),
])
def test_convert_struct_time_to_dt(arg, ret):
    assert _convert_struct_time_to_dt(arg) == ret


@patch("feedparser.parse", side_effect=[MOCK_ENTRIES])
def test_get_feed_entries(inp):
    first, last = tuple(get_feed_entries())

    assert first.date == date(year=2018, month=2, day=18)
    assert first.title == 'Twitter Digest 2018 Week 08'
    assert first.link == 'https://pybit.es/twitter_digest_201808.html'
    expected = ['flask', 'python', 'regex', 'twitter']
    # allow list or set
    assert sorted(list(first.tags)) == expected

    assert last.date == date(year=2017, month=1, day=6)
    assert last.title == 'Copy and Paste with Pyperclip'
    assert last.link == 'https://pybit.es/pyperclip.html'
    expected = ['code', 'pybites', 'python', 'tips', 'tricks']
    assert sorted(list(last.tags)) == expected


@pytest.mark.parametrize("arg, ret", [
    ('blabla', False),
    ('tricks', True),
    ('TRICKS', True),  # case should not matter
    ('TriCkS', True),
    ('python', False),  # whole term only so python != pythonic
    ('matplotlib&pandas', True),
    ('matplotlib&pandas&collections', True),
    ('matplotlib&pandas&flask', False),
    ('matplotlib|flask', True),
    ('matplotlib|django|flask', True),
    ('pyramid|django|flask', False),
])
def test_filter_entries_by_tag(arg, ret):
    entry = Entry(date=date(2016, 12, 22),
                  title='2016 py articles and useful books',
                  link='https://pybit.es/py-articles-books2016.html',
                  tags={'pythonic', 'data science',
                        'tips', 'tricks', 'matplotlib',
                        'pandas', 'books', 'collections'})
    assert filter_entries_by_tag(arg, entry) is ret


@patch("feedparser.parse", side_effect=[MOCK_ENTRIES])
@patch("builtins.input", side_effect=['pycon', 'twitter', 'python', 'nonsense',
                                      'python|regex', 'python&regex', 'REGeX',
                                      '', 'q'])
def test_main(entries, inp, capfd):
    main()
    out, _ = capfd.readouterr()

    output = [line for line in out.split('\n') if line.strip()]
    expected = ['0 entries matched', 'Twitter Digest 2018 Week 08',
                '1 entry matched', 'Copy and Paste with Pyperclip',
                'Twitter Digest 2018 Week 08', '2 entries matched',
                '0 entries matched', 'Copy and Paste with Pyperclip',
                'Twitter Digest 2018 Week 08', '2 entries matched',
                'Twitter Digest 2018 Week 08', '1 entry matched',
                'Twitter Digest 2018 Week 08', '1 entry matched',
                'Please provide a search term', 'Bye']
    for line, exp in zip(output, expected):
        assert exp in line