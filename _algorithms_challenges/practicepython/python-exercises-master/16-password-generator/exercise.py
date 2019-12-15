#! /usr/bin/env python
import random
import string


def generatePass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.SystemRandom().choice(characters) for _ in range(length))

if __name__ == '__main__':
    length = int(raw_input('How long the password should be? '))
    passwd = generatePass(length)
    print('\nThe password generated is: \n%s\n'%passwd)
