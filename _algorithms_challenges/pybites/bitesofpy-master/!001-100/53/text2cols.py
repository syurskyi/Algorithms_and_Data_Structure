from itertools import zip_longest

COL_WIDTH = 20


def _divide_line(line: str, col_width: int = COL_WIDTH):
    words = line.split()
    result = []
    line = words[0]
    for word in words[1:]:
        line2 = line + ' ' + word
        if len(line2) > col_width:
            result.append(line)
            line = word
        else:
            line = line2
    result.append(line)
    return result


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    lines = [_divide_line(col) for col in (text.split('\n\n'))]
    rv = [' '.join(combination) for combination in zip_longest(*lines, fillvalue=' ')]
    return '\n'.join(rv)
