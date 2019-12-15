def can_capture(queens):
    return row_or_column_capture(queens) or diagonal_capture(queens)


def row_or_column_capture(queens):
    return  queens[0][0] == queens[1][0] or queens[0][1] == queens[1][1]


def diagonal_capture(queens):
    diff1 = ord(queens[0][0]) - ord(queens[1][0])
    diff2 = ord(queens[0][1]) - ord(queens[1][1])
    return abs(diff1) == abs(diff2)
