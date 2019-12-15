import string

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    result = []
    for n in names:
        if n[0] == QUIT_CHAR:
            break
        if len(set(n).intersection(set(string.digits))) > 0:
            continue
        if n[0] != IGNORE_CHAR:
            result.append(n)
        if len(result) == MAX_NAMES:
            break
    return result
