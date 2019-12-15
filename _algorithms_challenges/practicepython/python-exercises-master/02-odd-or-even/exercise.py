#! /usr/bin/env python

if __name__ == '__main__':
    number = int(raw_input('Give me a number: '))
    if number % 2:
        statement = 'The number is odd'
    else:
        statement = 'The number is even'

    print(statement)