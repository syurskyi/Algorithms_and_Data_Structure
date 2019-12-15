import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    if not all(tz in TIMEZONES for tz in timezones):
        raise ValueError('Time zone name error')
    utc = pytz.utc.localize(utc)
    return all(utc.astimezone(pytz.timezone(tz)).hour in MEETING_HOURS for tz in timezones)
