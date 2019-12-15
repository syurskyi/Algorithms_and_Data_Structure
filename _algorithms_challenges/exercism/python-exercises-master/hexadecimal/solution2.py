# An alternative solution emphasizing EAFP instead of LBYL
# (see https://docs.python.org/glossary.html#term-eafp)
# With no checks performed on the input, this solution is rather fast -
# though still slower than the built-in int(hexstring, base=16), of course.


hexchars_to_int = dict(zip('0123456789', range(10)))
hexchars_to_int.update(zip('abcdef', range(10, 16)))
hexchars_to_int.update(zip('ABCDEFG', range(10, 16)))


def hexa(hexstring):
    result = 0
    hex_of_lastseen = None
    try:
        for hex_of_lastseen in hexstring:
            result = result*16 + hexchars_to_int[hex_of_lastseen]
    except KeyError:
        # not a valid hexchar
        hex_of_lastseen = None
    if hex_of_lastseen is None:
        # hexstring was empty or triggered KeyError
        raise ValueError('Invalid hexadecimal string')
    return result
