#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
import os

def fileToArray(filePath):
    with open(filePath, 'r') as file:
        lines = []
        line = file.readline()
        while line:
            if line != '':
                lines.append(line.rstrip())
                line = file.readline()
        return lines



if __name__ == '__main__':
    cwd = os.getcwd()
    prime = cwd + '/23-file-overlap/prime.txt'
    happy = cwd + '/23-file-overlap/happy.txt'

    primes = fileToArray(prime)
    happies = fileToArray(happy)

    print('Primes: ' + str(primes) + '\n\nHappies: ' + str(happies))

    print('\n\nIntersection of both files are: '+ str(set(primes).intersection(happies)))