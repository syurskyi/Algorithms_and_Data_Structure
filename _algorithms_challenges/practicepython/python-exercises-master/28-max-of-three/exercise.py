#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
import random

def max(list):
    max = list[0]
    for el in list:
        if el > max:
            max = el
    return max

if __name__ == '__main__':
    random = random.sample(range(0,100), 3)

    print(random)
    print('MAX: %s'%max(random))
