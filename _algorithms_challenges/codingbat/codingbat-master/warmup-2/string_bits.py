''' Given a string, return a new string made of every other char starting with
the first, so "Hello" yields "Hlo". '''


def string_bits(str):
    new_str = ''
    for i, char in enumerate(str):
        if i % 2 == 0:
            new_str += char
    return new_str
