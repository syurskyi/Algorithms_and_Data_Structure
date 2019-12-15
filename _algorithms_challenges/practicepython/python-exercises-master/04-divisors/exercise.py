#! /urs/bin/env python

if __name__ == '__main__':
    number = int(raw_input('Give me a number: '))
    list = range(1,number/2 + 1)
    divisors = []
    for el in list:
        if number % el == 0:
            divisors.append(el)

    print('The divisors of ' + str(number) + ' are ' + str(divisors))
