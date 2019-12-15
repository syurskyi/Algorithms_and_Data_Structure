from omdb import (get_movie_data, get_single_comedy,
                  get_movie_most_nominations, get_movie_longest_runtime)

movies = get_movie_data()


def test_movie_data_structure():
    assert len(movies) == 5
    assert all(type(m) == dict for m in movies)


def test_data_analysis():
    assert get_single_comedy(movies) == 'Horrible Bosses'
    assert get_movie_most_nominations(movies) == 'Fight Club'
    assert get_movie_longest_runtime(movies) == 'Blade Runner 2049'