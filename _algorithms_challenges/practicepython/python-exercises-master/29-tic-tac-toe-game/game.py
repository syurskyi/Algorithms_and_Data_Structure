import sys


class TicTacToe:
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    movesCount = 0
    result = ''

    def __init__(self):
        self.welcome(self)
        self.startGame()

    @staticmethod
    def welcome(self):
        print('''
        
  _____ _      _____          _____          
 |_   _(_)__  |_   _|_ _ __  |_   _|__  ___  
   | | | / _|   | |/ _` / _|   | |/ _ \/ -_) 
   |_| |_\__|   |_|\__,_\__|   |_|\___/\___| 
                                             
        
        Player one begins!
        
        ''')
        self.displayBoard()

    def startGame(self):
        move = self.askForMove()
        self.updateGame(move)
        self.tick()

    def tick(self):
        self.checkWinner()
        self.displayBoard()
        self.startGame()

    def askForMove(self):
        line = ''
        if self.movesCount % 2 == 1:
            line = 'Player two move (x,y) : '
        else:
            line = 'Player one move (x,y) : '

        move = str(input(line)).split(',')
        while not self.validate(move):
            move = str(input(line)).split(',')

        return move

    def displayBoard(self):
        """
            Function printing the board of the game
        """
        print(' --- ' * len(self.game[0]))
        for row in self.game:
            print('|', end='')
            for record in row:
                print(' ' + str(record) + '  |', end='')
            print('\n', end='')
        print(' --- ' * len(self.game[0]))
        return self

    def updateGame(self, move):
        oX = int(move[0]) - 1
        oY = int(move[1]) - 1
        self.game[oX][oY] = self.movesCount % 2 + 1
        self.movesCount += 1
        return self

    def checkWinner(self):
        """
            Function checking who is the winner of the game
        """
        # vertical/horizontal
        for i in range(3):
            h = self.game[i][0] * self.game[i][1] * self.game[i][2]
            v = self.game[0][i] * self.game[1][i] * self.game[2][i]
            if v == 1 or h == 1:
                self.result = 1
            if v == 8 or h == 8:
                self.result = 2

        # diagonals
        d1 = self.game[0][0] * self.game[1][1] * self.game[2][2]
        d2 = self.game[0][2] * self.game[1][1] * self.game[2][0]

        if d1 == 1 or d2 == 1:
            self.result = 1
        if d1 == 8 or d2 == 8:
            self.result = 2

        self.checkIfDraw()

        if self.result != '' and self.result != 0:
            print('The winner is player %s' % self.result)
            sys.exit('Congratulations!')
        if self.result == 0:
            self.displayBoard()
            sys.exit('It is a draw!')

        return self

    def checkIfDraw(self):
        if self.allSlotsFull() and self.result != 1 and self.result != 2:
            self.result = 0

    def allSlotsFull(self):
        full = 0
        for row in self.game:
            for record in row:
                if int(record) != 0:
                    full += 1
        if full == 9:
            return True
        return False

    def validate(self, move):
        oX = int(move[0]) - 1
        oY = int(move[1]) - 1
        if self.game[oX][oY] != 0:
            return False
        return True

