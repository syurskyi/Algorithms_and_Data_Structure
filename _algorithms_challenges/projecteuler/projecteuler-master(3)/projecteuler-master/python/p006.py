#!/usr/bin/env python

"""Problem 6: Sum square difference"""

def main():
    lim = 100
    square_of_sum = (lim*(lim+1)//2) ** 2 # arithmetic progression
    sum_of_squares = (2*lim+1)*(lim+1)*lim//6
    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    print(main())
