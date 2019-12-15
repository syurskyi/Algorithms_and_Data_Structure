import csv
from collections import Counter, defaultdict
from io import StringIO
import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content: str):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    lines = defaultdict(lambda : Counter())
    for row in [{'episode': x['Episode'], 'character': x['Character'],
                 'words': len(x['Line'].split())} for x in csv.DictReader(StringIO(content))]:
        lines[row['character']] += Counter({row['episode']: row['words']})
    return lines
