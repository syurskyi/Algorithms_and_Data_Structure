from collections import defaultdict
from directors import (get_movies_by_director, get_average_scores,
                       calc_mean_score, Movie)

director_movies = get_movies_by_director()


def test_get_movies_by_director():
    assert 'Sergio Leone' in director_movies
    assert len(director_movies['Sergio Leone']) == 4
    assert len(director_movies['Peter Jackson']) == 12


def test_director_movies_data_structure():
    assert type(director_movies) in (dict, defaultdict)
    assert type(director_movies['Peter Jackson']) == list
    assert type(director_movies['Peter Jackson'][0]) == Movie


def test_calc_mean_score():
    movies_sergio = director_movies['Sergio Leone']
    movies_nolan = director_movies['Christopher Nolan']
    assert calc_mean_score(movies_sergio) == 8.5
    assert calc_mean_score(movies_nolan) == 8.4


def test_get_average_scores():
    # top 2
    scores = get_average_scores(director_movies)

    assert scores[0] == ('Sergio Leone', 8.5)
    assert scores[1] == ('Christopher Nolan', 8.4)

    # order / score might slightly change depending the way the mean
    # is calculated so only test director names in top scores
    directors = {score[0] for score in scores[2:13]}

    assert 'Quentin Tarantino' in directors
    assert 'Hayao Miyazaki' in directors
    assert 'Frank Darabont' in directors
    assert 'Stanley Kubrick' in directors
    assert 'James Cameron' in directors
    assert 'Joss Whedon' in directors
    assert 'Alejandro G. Iñárritu' in directors