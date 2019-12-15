#! /urs/bin/env python
def isPrimary(number):
    list = range(2,number/2 + 1)
    primary = True
    for el in list:
        if number % el == 0:
            primary = False
            break

    if primary:
        print('%s is a primary number!'%number)
    else:
        print('%s is not a primary number!'%number)

if __name__ == '__main__':
    number = int(raw_input('Give me a number: '))
    isPrimary(number)


