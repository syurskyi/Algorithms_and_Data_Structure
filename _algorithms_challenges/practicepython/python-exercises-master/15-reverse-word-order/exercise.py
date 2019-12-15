#! /usr/bin/env python


def reverseOrder(string):
    parts = string.split(' ')
    result = ''
    for word in reversed(parts):
        result+= str(word) +  ' '

    return result


if __name__ == '__main__':
    words = str(raw_input('Give me a sentence: '))
    result = reverseOrder(words)
    print(result)
