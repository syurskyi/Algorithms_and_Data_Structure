import os
import re
from collections import Counter
from urllib.request import urlretrieve
from dateutil.parser import parse

commits = os.path.join('/tmp', 'commits')
urlretrieve('https://bit.ly/2H1EuZQ', commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    ##
    # Example log line:
    # Date:   Tue Mar 5 22:34:33 2019 +0100 | 2 files changed, 4 insertions(+), 4 deletions(-)
    # Groups:    (                         )                  ( )              ( )
    log_regex = re.compile(
        r'^Date: +\w+ (\w+ \d+ \d+:\d+:\d+ \d{4} [+-]\d{4}) .+ged(?:, (\d+) ins.*?)?(?:, (\d+) del.*?)?$',
        flags=re.MULTILINE)

    log = Counter()
    c = 0
    with open(commit_log) as cl:
        for x in log_regex.findall(cl.read()):
            c += 1
            dt = parse(x[0])
            if year is None or year == dt.year:
                log += Counter({(YEAR_MONTH.format(y=dt.year, m=dt.month)): int('0' + x[1]) - int('0' + x[2])})
    lst = sorted([(k, v) for k, v in log.items()], key=lambda x: x[1])
    return lst[0][0], lst[-1][0]
