import os
import urllib.request
import re
from collections import Counter

# data provided

stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)

WORD_REGEX = r"(['\w]+)"
word_regex = re.compile(WORD_REGEX)


def get_harry_most_common_word():
    with open(harry_text) as f:
        words = word_regex.findall(f.read().lower())
    with open(stopwords_file) as f:
        stops = word_regex.findall(f.read().lower())
    return Counter([x for x in words if x not in stops]).most_common(1)[0]
