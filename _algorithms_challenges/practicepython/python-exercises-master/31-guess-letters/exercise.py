#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
import os
import random
import sys


def getWord():
    cwd = os.getcwd()
    filePath = cwd + '/30-pick-word/sowpods.txt'
    with open(filePath, 'r') as file:
        lines = file.readlines()
        word = random.choice(lines).strip()
        return word


class HangMan:

    def __init__(self, word):
        self.word = word
        self.state = []
        self.generateState()
        self.guessCount = 0
        self.welcome()
        self.startGame()

    def generateState(self):
        for char in self.word:
            self.state.append('_')

    def startGame(self):
        guess = self.askForGuess()
        self.checkGuess(guess)
        self.goOn()

    def welcome(self):
        print('''
                                                
  /\  /\__ _ _ __   __ _    /\/\   __ _ _ __  
 / /_/ / _` | '_ \ / _` |  /    \ / _` | '_ \ 
/ __  / (_| | | | | (_| | / /\/\ \ (_| | | | |
\/ /_/ \__,_|_| |_|\__, | \/    \/\__,_|_| |_|
                   |___/                               
        
            Guess The word!
            
        ''')

    def askForGuess(self):
        guess = str(input('Guess a latter: ')).upper()
        self.guessCount += 1
        return guess

    def checkGuess(self, guess):
        countCorrect = 0
        for index, value in enumerate(self.word):
            if guess == value:
                self.state[index] = value
                countCorrect += 1
        if countCorrect != 0:
            print('You guessed!')
        else:
            print('Try again!')

    def goOn(self):
        self.displayState()
        guess = self.askForGuess()
        self.checkGuess(guess)
        self.checkIfWon()
        self.goOn()

    def displayState(self):
        for char in self.state:
            print(char, end='')
        print('\n')

    def checkIfWon(self):
        countCorrect = 0
        for index, value in enumerate(self.state):
            if value == self.word[index]:
                countCorrect += 1
        if countCorrect == len(self.word):
            sys.exit('You won!')


if __name__ == '__main__':
    word = getWord()
    print(word)
    game = HangMan(word)
