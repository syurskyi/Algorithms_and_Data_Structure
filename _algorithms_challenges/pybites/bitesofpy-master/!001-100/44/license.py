import string
from random import choices

def gen_key(*, parts=4, chars_per_part=8):
    s = ''
    for part in range(parts):
        s += ''.join(choices(string.ascii_uppercase + string.digits,k=chars_per_part))+'-'
    return s[:-1]