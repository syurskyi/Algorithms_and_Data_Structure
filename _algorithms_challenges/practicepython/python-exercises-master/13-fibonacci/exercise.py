#! /usr/bin/env python

def generateFibbonaci(length):
    list = [1,1]

    for x in range(1, length - 1):
        list.append(list[x-1] + list[x])

    return list

if __name__ == '__main__':
    number = int(raw_input('How many fibonaccies ? '))
    result = generateFibbonaci(number)
    print('The fibonaccies are: ' + str(result))
