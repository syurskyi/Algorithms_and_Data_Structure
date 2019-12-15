#! /urs/bin/env python
import random

if __name__ == '__main__':
    list_1 = list(random.sample(range(0,20), random.randint(1,15)))
    list_2 = list(random.sample(range(0,20), random.randint(1,15)))
    print(str(list_1) + "\n" + str(list_2))
    common = set([elem for elem in list_1 if elem in list_2])

    print(str(list(common)))