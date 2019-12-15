''' Given 2 strings, a and b, return the number of the positions where they
contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since
the "xx", "aa", and "az" substrings appear in the same place in both
strings. '''


def string_match(a, b):
    count = 0
    if len(a) >= 2 and len(b) >= 2:
        for i in range((min(len(a), len(b))) - 1):
            if a[i] == b[i] and a[i + 1] == b[i + 1]:
                count += 1
    return count
