from similarity import get_similarities


def test_get_similarities():
    # cast to list in case of generator
    similar_tags = list(get_similarities())

    # not interested in the order of the pairs
    similar_tags = {tuple(sorted(pair)) for pair in similar_tags}

    expected = [('cheat sheet', 'cheat sheets'),
                ('python anywhere', 'pythonanywhere'),
                ('web scraping', 'webscraping'),
                ('object oriented', 'objectoriented'),
                ('web scraping', 'webscraping'),
                ('contextmanager', 'contextmanagers'),
                ('python anywhere', 'pythonanywhere'),
                ('contextmanager', 'contextmanagers'),
                ('magic methods', 'magicmethods'),
                ('magic methods', 'magicmethods'),
                ('code challenges', 'codechallenges'),
                ('cheat sheet', 'cheat sheets'),
                ('object oriented', 'objectoriented'),
                ('code challenges', 'codechallenges')]

    for hit in expected:
        assert tuple(sorted(hit)) in similar_tags, f'{hit} not in similar tags'