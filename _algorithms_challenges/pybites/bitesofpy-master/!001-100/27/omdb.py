import glob
import json
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    result = []
    for file in files:
        with open(file) as f:
            result.append(json.load(f))
    return result


def get_single_comedy(movies):
    return [m['Title'] for m in movies if 'Comedy' in m['Genre'].split(', ')][0]


def get_movie_most_nominations(movies):
    r = re.compile(r'(\d+) nomin')
    return sorted([(m['Title'], m['Awards']) for m in movies], key=lambda x: int(r.findall(x[1])[0]))[-1][0]


def get_movie_longest_runtime(movies):
    r = re.compile(r'(\d+) min')
    return sorted([(m['Title'], int(r.findall(m['Runtime'])[0])) for m in movies], key=lambda x: -x[1])[0][0]
