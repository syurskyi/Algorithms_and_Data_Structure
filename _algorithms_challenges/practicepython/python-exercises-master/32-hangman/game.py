import sys
import os

class HangMan:

    def __init__(self, word, hangmans):
        os.system('clear')
        self.hangmans = hangmans
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
        self.displayHangman()
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
        Press any key To Start
            
        ''')
        input()
        os.system('clear')

    def displayHangman(self):
        print(self.hangmans[self.guessCount])


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
        os.system('clear')
        self.displayHangman()
        self.displayState()
        guess = self.askForGuess()
        self.checkGuess(guess)
        self.checkIfWon()
        self.goOn()

    def displayState(self):
        for char in self.state:
            print(" " + char + " ", end='')
        print('\n')

    def checkIfWon(self):
        if self.guessCount == 6:
            sys.exit('You lose! The right word was: ' + self.word)
        countCorrect = 0
        for index, value in enumerate(self.state):
            if value == self.word[index]:
                countCorrect += 1
        if countCorrect == len(self.word):
            sys.exit('You won!')