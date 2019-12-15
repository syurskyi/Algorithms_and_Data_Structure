ROMAN_DIGITS = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if not isinstance(decimal_number, int) or not (0 < decimal_number < 4000):
        raise ValueError('Value out of range or not a number')
    res = ''
    d = decimal_number
    for v, c in ROMAN_DIGITS:
        if d >= v:
            x = d // v
            res += c * x
            d -= v * x
    return res
