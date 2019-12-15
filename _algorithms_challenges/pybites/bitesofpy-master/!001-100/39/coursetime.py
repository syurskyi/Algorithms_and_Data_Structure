from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join('/tmp', 'course_timings')
urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    result = []
    with open(COURSE_TIMES) as ct:
        for line in ct.readlines():
            times = re.findall(r'\((\d\d?:\d\d)\)', line)
            if len(times) > 0:
                result.append(times[0])
    return result


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total_time = sum(timedelta(minutes=xt.minute, seconds=xt.second).total_seconds()
                     for t in timestamps
                     for xt in [datetime.strptime(t, '%M:%S')])
    return str(timedelta(seconds=total_time))
