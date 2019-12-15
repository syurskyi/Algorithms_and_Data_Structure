import csv
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path('/tmp')
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats, encoding="utf-8-sig") as s:
        return [x[0] for x in sorted(
            [[round(float(x['Bite'].split(' ')[1])), float(x['Difficulty'])] for x in csv.DictReader(s, delimiter=';')
             if x['Difficulty'] != 'None'], key=lambda x: x[1], reverse=True)[:N]]


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)
