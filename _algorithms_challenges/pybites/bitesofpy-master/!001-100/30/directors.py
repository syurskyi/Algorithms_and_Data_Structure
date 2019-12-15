import csv
import os
from collections import defaultdict, namedtuple
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    with open(MOVIE_DATA) as f:
        reader = csv.DictReader(f)
        films = [{'director': r['director_name'], 'title': r['movie_title'], 'year': r['title_year'],
                  'score': r['imdb_score']}
                 for r in reader]
    result = defaultdict()
    for r in films:
        yr = int(r['year'], 10) if r['year'] else 0
        if yr >= MIN_YEAR:
            score = float(r['score']) if r['score'] else 0.0
            movie = Movie(r['title'], yr, score)
            if r['director'] in result:
                result[r['director']].append(movie)
            else:
                result[r['director']] = [movie]
    return result


def calc_mean_score(movies: list):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(sum(x.score for x in movies) / len(movies), 1)


def get_average_scores(directors: defaultdict):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    return sorted([(d, calc_mean_score(directors[d])) for d in directors.keys() if len(directors[d]) >= MIN_MOVIES],
                  key=lambda x: -x[1])
