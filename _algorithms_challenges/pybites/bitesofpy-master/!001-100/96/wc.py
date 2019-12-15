def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    lines = words = chars = 0
    with open(file_) as f:
        for line in f.readlines():
            lines += 1
            words += len(line.split())
            chars += len(line)
    return f'{lines} {words} {chars} {file_}'
