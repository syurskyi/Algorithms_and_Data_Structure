from collections import namedtuple, Counter
import re
from datetime import datetime
from time import strptime, strftime
from typing import NamedTuple

import feedparser

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'https://bites-data.s3.us-east-2.amazonaws.com/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


class PythonBytes:

    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(URL).entries

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        for i in self.entries:
            if domain in i.summary_detail.value:
                yield i.itunes_episode

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        dom_count = Counter()
        for i in self.entries:
            domains = set(re.findall(r'https?://[^/]+', i.summary_detail.value)) - IGNORE_DOMAINS
            dom_count.update(domains)
        return dom_count.most_common(n)

    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        return sum(1 for i in self.entries if SPECIAL_GUEST in i.summary_detail.value)

    def _time_to_secs(self, tm: str) -> int:
        parts = [int(s) for s in tm.split(':')]
        return (parts[0] * 60 + parts[1]) * 60 + parts[2]

    def _secs_to_time(self, sec: int) -> str:
        t, s = divmod(sec, 60)
        h, m = divmod(t, 60)
        return f'{h:02}:{m:02}:{s:02}'

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        # res = Duration('', self.entries[0].itunes_duration, self.entries.entries[0].itunes_duration)
        min_t = max_t = self._time_to_secs(self.entries[0].itunes_duration)
        total_t = min_t
        for i in self.entries[1:]:
            _t = self._time_to_secs(i.itunes_duration)
            total_t += _t
            if _t < min_t:
                min_t = _t
            elif _t > max_t:
                max_t = _t
        return Duration(total_t // len(self.entries),
                        self._secs_to_time(max_t),
                        self._secs_to_time(min_t))
