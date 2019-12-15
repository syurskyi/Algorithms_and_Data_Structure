from datetime import datetime, timedelta

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    delay = delay_time.split()
    td = start_time
    for dl in delay:
        if dl[-1] == 'd':
            td += timedelta(days=int(dl[:-1]))
        elif dl[-1] == 'h':
            td += timedelta(hours=int(dl[:-1]))
        elif dl[-1] == 'm':
            td += timedelta(minutes=int(dl[:-1]))
        elif dl[-1] == 's':
            td += timedelta(seconds=int(dl[:-1]))
        else:
            td += timedelta(seconds=int(dl))
    return f'{task} @ {td.strftime("%Y-%m-%d %H:%M:%S")}'
