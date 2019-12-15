#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
import os

if __name__ == '__main__':
    cwd = os.getcwd()
    filePath = cwd + '/22-read-from-file/file.txt'
    namesCount = 0
    with open(filePath, 'r') as open_file:
        line = open_file.readline()
        while line:
            namesCount += 1
            line = open_file.readline()

    print('There are %s names in file.txt' % namesCount)
