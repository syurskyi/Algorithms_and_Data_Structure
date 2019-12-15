''' Return the number of times that the string "hi" appears anywhere in the
given string. '''


def count_hi(str):
    count = 0
    for i, _ in enumerate(str):
        if str[i:i + 2] == 'hi':
            count += 1
    return count
