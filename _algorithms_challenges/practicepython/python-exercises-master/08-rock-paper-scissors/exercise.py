#! /urs/bin/env python
import random

if __name__ == '__main__':
    options = ['rock','paper','scissors']

    while True:
        player = str(raw_input('You choice(rock, paper, scissors): '))
        opponent = str(options[random.randint(0,2)])

        if player == options[0] and opponent == options[2]:
            print('Conrates! You won! (%s,%s)'%(player, opponent))
            break
        elif player == options[1] and opponent == options[0]:
            print('Conrates! You won!(%s,%s)'%(player, opponent))
            break
        elif player == options[2] and opponent == options[1]:
            print('Conrates! You won!(%s,%s)'%(player, opponent))
            break
        elif player == opponent:
            print("It's a draw! Try again. (%s,%s)"%(player, opponent))
            break
        else:
            print('You loose :/ Try again! (%s,%s)'%(player, opponent))
            break