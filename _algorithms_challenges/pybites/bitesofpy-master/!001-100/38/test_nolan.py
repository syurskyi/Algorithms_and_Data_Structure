import xml.etree.ElementTree as ET

from Previous.nolan import get_tree, get_movies, get_movie_longest_runtime


def test_get_tree():
    tree = get_tree()
    assert type(tree) in (ET.ElementTree, ET.Element)
    assert len(list(tree.iter(tag='movie'))) == 5


def test_get_movies():
    assert list(get_movies()) == ['The Prestige', 'The Dark Knight',
                                  'The Dark Knight Rises', 'Dunkirk',
                                  'Interstellar']


def test_get_movie_longest_runtime():
    assert get_movie_longest_runtime() == 'Interstellar'