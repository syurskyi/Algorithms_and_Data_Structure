from tags import get_pybites_top_tags


def test_get_pybites_top_tags():
    expected = [('python', 79),
                ('learning', 79),
                ('codechallenges', 72),
                ('twitter', 62),
                ('tips', 61),
                ('flask', 52),
                ('news', 49),
                ('django', 37),
                ('code', 25),
                ('github', 24)]
    assert get_pybites_top_tags() == expected