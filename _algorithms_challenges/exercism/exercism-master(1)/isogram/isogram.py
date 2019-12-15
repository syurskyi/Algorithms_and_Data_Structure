import re

def is_isogram(string):
    s = re.sub("[- ]", "", string.lower())
    return len(set(s)) == len(s)
