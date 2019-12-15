"""In this Bite you will use ElementTree to parse some Nolan movies we extracted from OMDb.

Luckily most APIs switched to JSON, but sometimes XML is all there is, so at least learn to parse some! Complete the get_tree, get_movies and get_movie_longest_runtime functions below. See the docstrings and tests for more info.

Have fun and remember:

Keep calm and code in Python!"""

import xml.etree.ElementTree as ET

# from OMDB
xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>'''  # noqa E501


def get_tree():
    """You probably want to use ET.fromstring"""
    return ET.ElementTree(ET.fromstring(xmlstring))


def get_movies():
    """Call get_tree and retrieve all movie titles, return a list or generator"""
    tree = get_tree()
    for movie in tree.iter(tag='movie'):
        yield movie.attrib['title']


def _get_runtime(movie):
    """Helper function to extract the minutes (int) from the runtime movie attribute"""
    return int(movie.attrib['runtime'].rstrip(' min'))


def get_movie_longest_runtime():
    """Call get_tree again and return the movie with the longest runtime in minutes,
       for latter consider adding a _get_runtime helper"""
    tree = get_tree()
    movies = [(movie.attrib['title'], _get_runtime(movie))
              for movie in tree.iter(tag='movie')]
    max_movie, max_runtime = max(movies, key=lambda m: m[1])
    return max_movie