from random import randint
from collections import namedtuple

from transpose import transpose

POSTS = {'2017-8': 19, '2017-9': 13, '2017-10': 13,
         '2017-11': 12, '2017-12': 11, '2018-1': 3}
NAMES = ['Bob', 'Julian', 'Tim', 'Carmen', 'Henk', 'Sofia', 'Bernard']

Member = namedtuple('Member', 'name since_days karma_points bitecoin_earned')


def _gen_community():
    for name in NAMES:
        yield Member(name=name,
                     since_days=randint(1, 365),
                     karma_points=randint(1, 100),
                     bitecoin_earned=randint(1, 100))


def test_transpose_dict():
    months, num_posts = transpose(POSTS)
    assert list(months) == ['2017-8', '2017-9', '2017-10',
                            '2017-11', '2017-12', '2018-1']
    assert list(num_posts) == [19, 13, 13, 12, 11, 3]


def test_transpose_list_tuplies():
    community = list(_gen_community())
    names, days, karma, bitecoin = transpose(community)
    assert list(names) == NAMES
    assert list(days) == [m.since_days for m in community]
    assert list(karma) == [m.karma_points for m in community]
    assert list(bitecoin) == [m.bitecoin_earned for m in community]