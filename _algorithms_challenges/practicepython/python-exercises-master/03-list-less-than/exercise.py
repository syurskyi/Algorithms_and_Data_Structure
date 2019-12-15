#! /usr/bin/env python

if __name__ == '__main__':
    list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    result = []
    for el in list:
        if el < 5:
            result.append(el)

    print(result)