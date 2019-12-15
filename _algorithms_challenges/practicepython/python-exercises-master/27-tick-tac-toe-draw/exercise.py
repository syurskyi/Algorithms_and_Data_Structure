#! /Users/piotrjankiewicz/anaconda3/bin/python3.6

def board(game):
    print(' --- '*len(game[0]))
    for row in game:
        print('|', end='')
        for record in row:
            print(' ' + str(record) + '  |', end='')
        print('\n', end='')
    print(' --- '*len(game[0]))

def updateGameState(game,move):
    game[int(move[0]) - 1][int(move[1]) - 1] = 1
    return game


if __name__ == '__main__':
    game = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    board(game)
    move = str(input('Your move (x,y) : ')).split(',')
    game = updateGameState(game,move)
    board(game)