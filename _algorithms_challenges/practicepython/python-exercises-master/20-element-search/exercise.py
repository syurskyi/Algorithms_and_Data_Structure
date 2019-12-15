#! /usr/bin/env python
import numpy as np


def binarySearch(element, list):
    currentIndex = len(list) / 2
    if currentIndex < 2:
        print('Element is not in the list :/')
    elif element < list[currentIndex]:
        binarySearch(element, list[0:currentIndex])
    elif element > list[currentIndex]:
        binarySearch(element, list[currentIndex:len(list) - 1])
    elif element == list[currentIndex]:
        print('Element is in the list!')


if __name__ == '__main__':
    list = list(np.random.choice(100, 20, replace=True))
    list.sort()
    print(str(list))
    number = int(input('Look for: '))
    binarySearch(number, list)
