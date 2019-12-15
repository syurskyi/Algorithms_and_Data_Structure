from functools import reduce


valid_hexchars = set('0123456789abcdef')


def hexa(hexstring):
    s = hexstring.lower()
    if not s or set(s) - valid_hexchars:
        raise ValueError('Invalid hexadecimal string')
    hexchars_as_ints = [
        ord(c) - ord('a') + 10 if c in 'abcdef' else ord(c) - ord('0')
        for c in s
        ]
    return reduce(lambda x, y: x * 16 + y, hexchars_as_ints, 0)
