from collections import namedtuple
from datetime import datetime
import json

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
BlogTuple = namedtuple('BlogTuple', 'name founders started tags location site')


def dict2nt(dict_):
    return BlogTuple(**dict_)


def nt2json(nt):
    return json.dumps(nt._asdict(), default=lambda x: x.isoformat() if isinstance(x, datetime) else None)
