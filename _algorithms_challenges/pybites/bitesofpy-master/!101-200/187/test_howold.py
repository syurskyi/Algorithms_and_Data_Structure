import pytest

from howold import Actor, Movie, get_age


actors = [
    Actor('Wesley Snipes', 'July 31, 1962'),
    Actor('Robert de Niro', 'August 17, 1943'),
    Actor('Jennifer Aniston', 'February 11, 1969'),
    Actor('Mikey Rourke', 'September 16, 1952'),
    Actor('Al Pacino', 'July 31, 1962'),
    Actor('Alec Baldwin', 'July 31, 1962'),
    Actor('Michelle Pfeiffer', 'April 29, 1958'),
]
movies = [
    Movie('New Jack City', 'January 17, 1991'),
    Movie('Goodfellas', 'October 19, 1990'),
    Movie('Horrible Bosses', 'September 16, 2011'),
    Movie('Harley Davidson and the Marlboro Man', 'December 28, 1991'),
    Movie('Heat', 'December 15, 1995'),
    Movie('Glengarry Glen Ross', 'September 29, 1992'),
    Movie('Scarface', 'March 12, 1984'),
]
return_strings = [
    'Wesley Snipes was 28 years old when New Jack City came out.',
    'Robert de Niro was 47 years old when Goodfellas came out.',
    'Jennifer Aniston was 42 years old when Horrible Bosses came out.',
    'Mikey Rourke was 39 years old when Harley Davidson and the Marlboro Man came out.',  # noqa E501
    'Al Pacino was 33 years old when Heat came out.',
    'Alec Baldwin was 30 years old when Glengarry Glen Ross came out.',
    'Michelle Pfeiffer was 25 years old when Scarface came out.',
]


@pytest.mark.parametrize('actor, movie, expected',
                         zip(actors, movies, return_strings))
def test_get_age(actor, movie, expected):
    assert get_age(actor, movie) == expected