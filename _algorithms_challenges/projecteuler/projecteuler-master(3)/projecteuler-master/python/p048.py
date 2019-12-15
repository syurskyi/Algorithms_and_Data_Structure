#!/usr/bin/env python

"""Problem 48: Self powers"""

def main():
    return sum([pow(i, i, 10**10) for i in range(1, 1001)]) % 10**10

if __name__ == "__main__":
    print(main())
