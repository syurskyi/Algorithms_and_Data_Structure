#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
import os
import random

def countWords(uri):
    count = 0
    with open(filePath, 'r') as open_file:
        line = open_file.readline()
        while line:
            count += 1
            line = open_file.readline()
    return count

def getWord(int, filePath):
    count = 0
    with open(filePath, 'r') as open_file:
        line = open_file.readline()
        while line:
            count += 1
            line = open_file.readline()
            if count == int:
                result = line
                line = False
    return result

if __name__ == '__main__':
    cwd = os.getcwd()
    filePath = cwd + '/30-pick-word/sowpods.txt'
    with open(filePath, 'r') as file:
        lines = file.readlines()
        word = random.choice(lines).strip()
        print(word)
    # len = countWords(filePath)
    # random = random.randint(0,len+1)
    # word = getWord(random, filePath)
    # print(word, end= '')
