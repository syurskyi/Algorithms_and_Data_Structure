import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    try:
        d = open(DICTIONARY,'r')
        result = d.read().splitlines()
    except IOError:
        result = []
    finally:
        d.close()

    return result


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    result = 0
    for l in word:
        lu = l.upper()
        result += LETTER_SCORES[lu] if lu in LETTER_SCORES else 0
    return result


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    if words is None or len(words) == 0:
        raise ValueError()
    lst = {word:calc_word_value(word) for word in words}
    result = sorted(lst.items(),key=lambda x:-x[1])[0]
    return result[0]

#words = load_words()

#print('word count %d' % len(words))
