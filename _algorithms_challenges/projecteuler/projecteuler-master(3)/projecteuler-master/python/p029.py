#!/usr/bin/env python

"""Problem 29: Distinct powers"""

def main():
    return len({a**b for a in range(2, 101) for b in range(2, 101)})

if __name__ == "__main__":
    print(main())
