import re


def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    t = re.match(r'^( *)', text)
    return len(t.group(0))