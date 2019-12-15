# /#! /urs/bin/env python

if __name__ == '__main__':
    all = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    odd = [number for number in all if number % 2 == 1]
    even = [number for number in all if number % 2 == 0]

    print("All: " + str(all) + '\nOdd: ' + str(odd))
