#! /urs/bin/env python
import random

if __name__ == '__main__':
    number = random.randint(0,9)
    attempts = 0

    while True:
        player = (raw_input('Guess the number from 0 to 9: '))
        if player == 'exit':
            break
        player = int(player)
        attempts+=1

        if player == number:
            print('Conrates! You guessed!\n')
            break
        elif player != number:
            if number > player:
                print('To low!\n')
            else:
                print('To high!\n')


    print('Number of attempts: %s. Bye!'%attempts )