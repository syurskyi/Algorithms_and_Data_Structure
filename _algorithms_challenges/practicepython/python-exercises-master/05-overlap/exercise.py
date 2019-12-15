#/#! /urs/bin/env python
import random

if __name__ == '__main__':
    list_1 = []
    list_2 = []
    for a in range(0,40):
        list_1.append(random.randint(0,40))
        list_2.append(random.randint(0,40))

    print('List 1: '+str(list_1) + '\nList 2: ' + str(list_2))

    list_1 = set(list_1)
    list_2 = set(list_2)

    match = []

    for el in list_1:
        if el in list_2:
            match.append(el)

    print('The overlaped numbers are: ' + str(list(set(match))))