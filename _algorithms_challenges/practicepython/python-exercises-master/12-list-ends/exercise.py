#! /usr/bin/env python
import random


def firstAndLast(list):
    return [list[0], list[-1]]


if __name__ == '__main__':
    list = random.sample(range(0, 100), random.randint(1, 20))
    print('List: ' + str(list) + '\n')
    result = firstAndLast(list)
    print('First and Last: ' + str(result))
