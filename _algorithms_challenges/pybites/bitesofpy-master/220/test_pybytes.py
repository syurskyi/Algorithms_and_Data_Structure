import pytest

from pybytes import Duration, PythonBytes

REAL_PYTHON = "realpython.com"
PYBITES = 'pybit.es'


@pytest.fixture(scope="module")
def pb():
    return PythonBytes()


def test_get_episodes_pybites_was_mentioned(pb):
    actual = pb.get_episode_numbers_for_mentioned_domain(PYBITES)
    expected = ['106', '98', '34', '26', '14']
    assert sorted(actual) == sorted(expected)


def test_get_episodes_realpython_was_mentioned(pb):
    actual = pb.get_episode_numbers_for_mentioned_domain(REAL_PYTHON)
    expected = ['143', '134', '123', '119', '118', '114', '110', '102',
                '100', '97', '88', '86', '85', '84', '83', '82', '80', '76',
                '75', '71', '66', '56', '37', '20', '7']
    assert sorted(actual) == sorted(expected)


def test_number_episodes_with_special_guests(pb):
    actual = pb.number_episodes_with_special_guest()
    expected = 17
    assert actual == expected


def test_number_episodes_with_special_guests_half_feed(pb):
    """To prevent hardcoding the answer"""
    org_entries = pb.entries
    pb.entries = pb.entries[:20]
    actual = pb.number_episodes_with_special_guest()
    expected = 7
    pb.entries = org_entries  # pb is module scope so restore entries
    assert actual == expected


def test_get_most_mentioned_domain_names_default_top_15(pb):
    actual = pb.get_most_mentioned_domain_names()
    expected = [('https://github.com', 120),
                ('https://www.youtube.com', 50),
                ('https://medium.com', 38),
                ('https://www.python.org', 26),
                ('https://www.reddit.com', 26),
                ('https://docs.python.org', 25),
                ('https://realpython.com', 24),
                ('https://hackernoon.com', 22),
                ('https://pypi.python.org', 20),
                ('https://pypi.org', 16),
                ('https://en.wikipedia.org', 14),
                ('https://pragprog.com', 13),
                ('https://docs.pytest.org', 11),
                ('http://rollbar.com', 11),
                ('https://dbader.org', 9)]
    assert actual == expected


def test_get_most_mentioned_domain_names_top_5(pb):
    actual = pb.get_most_mentioned_domain_names(n=5)
    expected = [('https://github.com', 120),
                ('https://www.youtube.com', 50),
                ('https://medium.com', 38),
                ('https://www.python.org', 26),
                ('https://www.reddit.com', 26)]
    assert actual == expected


def test_average_episode_duration_full_feed(pb):
    actual = pb.get_average_duration_episode_in_seconds()
    max_, min_ = '00:56:54', '00:15:27'
    expected = Duration(avg=1439, max_=max_, min_=min_)
    # depending the way mean is calculated, results might differ
    expected_alt = Duration(avg=1442, max_=max_, min_=min_)
    assert actual in (expected, expected_alt)


def test_average_episode_duration_half_feed(pb):
    """To prevent hardcoding the answer"""
    num_half_episodes = int(len(pb.entries) / 2)
    org_entries = pb.entries
    pb.entries = pb.entries[:num_half_episodes]
    actual = pb.get_average_duration_episode_in_seconds()
    max_, min_ = '00:56:54', '00:16:40'
    expected = Duration(avg=1606, max_=max_, min_=min_)
    # depending the way mean is calculated, results might differ
    expected_alt = Duration(avg=1607, max_=max_, min_=min_)
    pb.entries = org_entries  # pb is module scope so restore entries
    assert actual in (expected, expected_alt)
