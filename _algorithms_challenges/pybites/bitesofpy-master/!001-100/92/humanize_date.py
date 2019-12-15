from collections import namedtuple
from datetime import datetime

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date: datetime):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime) or date > NOW:
        raise ValueError('pretty_date() only accepts datetime objects in the past')
    diff = NOW - date
    seconds = int(diff.total_seconds())
    minutes = seconds // 60
    hours = minutes // 60
    # This doesn't _feel_ very pythonic…
    if seconds < 10:
        return 'just now'
    if seconds < 60:
        return f'{seconds} seconds ago'
    if minutes < 2:
        return 'a minute ago'
    if minutes < 60:
        return f'{minutes} minutes ago'
    if hours < 2:
        return 'an hour ago'
    if hours < 24:
        return f'{hours} hours ago'
    if hours < 48:
        return 'yesterday'
    return date.strftime('%m/%d/%y')
