''' Given two strings, return True if either of the strings appears at the very
end of the other string, ignoring upper/lower case differences (in other words,
the computation should not be "case sensitive"). Note: s.lower() returns the
lowercase version of a string. '''


def end_other(a, b):
    match = False
    if a.lower() == b[-len(a):].lower():
        match = True
    if b.lower() == a[-len(b):].lower():
        match = True
    return match
