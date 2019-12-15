#! /usr/bin/env python
import random
import numpy as np


def removeDuplicates(list):
    result = []
    for el in list:
        if el not in result:
            result.append(el)

    return result


if __name__ == '__main__':
    list = list(np.random.choice(5, 8, replace=True))
    result = removeDuplicates(list)
    print('List: ' + str(list) + '\nNo dups: ' + str(result))
