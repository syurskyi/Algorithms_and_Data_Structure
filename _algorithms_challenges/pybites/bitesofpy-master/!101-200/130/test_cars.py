from cars import most_prolific_automaker, get_models


def test_most_prolific_automaker_1999():
    assert most_prolific_automaker(1999) == 'Dodge'


def test_most_prolific_automaker_2008():
    assert most_prolific_automaker(2008) == 'Toyota'


def test_most_prolific_automaker_2013():
    assert most_prolific_automaker(2013) == 'Hyundai'


def test_get_models_volkswagen():
    models = get_models('Volkswagen', 2008)
    # sets are unordered
    assert len(models) == 2
    assert 'Jetta' in models
    assert 'Rabbit' in models


def test_get_models_nissan():
    assert get_models('Nissan', 2000) == {'Pathfinder'}


def test_get_models_open():
    # not in data set
    assert get_models('Opel', 2008) == set()


def test_get_models_mercedes():
    models = get_models('Mercedes-Benz', 2007)
    assert len(models) == 3
    assert 'SL-Class' in models
    assert 'GL-Class' in models
    assert 'CL-Class' in models
