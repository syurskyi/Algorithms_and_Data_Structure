#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
import os
import random
import sys
from hangmans import getHangMans
from game import HangMan



def getWord():
    cwd = os.getcwd()
    filePath = cwd + '/30-pick-word/sowpods.txt'
    with open(filePath, 'r') as file:
        lines = file.readlines()
        word = random.choice(lines).strip()
        return word

if __name__ == '__main__':
    word = getWord()
    hangmans = getHangMans()
    print(word)
    game = HangMan(word, hangmans)
