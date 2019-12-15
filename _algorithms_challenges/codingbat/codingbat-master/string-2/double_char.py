''' Given a string, return a string where for every char in the original,
there are two chars. '''


def double_char(str):
    new_str = ''
    for char in str:
        new_str += 2 * char
    return new_str
