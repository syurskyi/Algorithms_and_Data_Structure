from collections import Counter
from urllib.request import urlretrieve
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

if not PYCON_HTML.exists():
    urlretrieve(PYCON_PAGE, PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    if soup is None:
        soup = _get_soup()
    speaker_tags = soup.find_all(class_='speaker')
    speaker_list = [speaker.strip().split(' ') for speakers in speaker_tags for speaker in
                    speakers.string.replace('/', ',').split(',')]
    return [first for first, *_ in speaker_list]


def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    det = gender.Detector()
    gender_counts = Counter(det.get_gender(name) for name in first_names)

    female_count = (gender_counts['female'] + gender_counts['mostly_female'])
    everyone_count = sum(n for _, n in gender_counts.items())

    return round(female_count / everyone_count * 100.0, 2)


if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)
