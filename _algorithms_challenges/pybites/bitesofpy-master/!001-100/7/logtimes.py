from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    parts = line.split()
    return datetime.strptime(parts[1], "%Y-%m-%dT%H:%M:%S")


def time_between_shutdowns(loglines: list):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    test_len = len(SHUTDOWN_EVENT)
    shutdowns = [datetime.strptime(l[1], "%Y-%m-%dT%H:%M:%S")
                 for l in [l.split(maxsplit=3) for l in loglines]
                 if l[3][:test_len] == SHUTDOWN_EVENT]
    return shutdowns[-1] - shutdowns[0]
