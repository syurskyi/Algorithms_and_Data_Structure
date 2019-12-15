#! /usr/bin/env python
import random
import sys

generated = (str(random.randint(0, 9999)).zfill(4))
print(generated)
totalCount = 0


def cowAndBulls(counter):
    player = (str(input("Please enter your guess between 0000 to 9999: ")).zfill(4))
    cows = 0
    bulls = 0

    for i in range(0, 4):
        generatedVal = generated[i]
        playersVal = player[i]

        if generatedVal == playersVal:
            cows += 1
        else:
            bulls += 1

    # for index, value in enumerate(player):
    #     if value in str(player)[index:]:
    #         if value == str(player)[index]:
    #             cows += 1
    #     else:
    #         if value in str(player):
    #             bulls += 1

    print("cows: %s,bulls: %s" % (cows, bulls))
    counter += 1

    if cows == 4:
        print('You win! The guess was: %s' % generated)
        sys.exit()

    cowAndBulls(counter)


if __name__ == '__main__':
    print('Welcome to cows and bulls!\n')
    cowAndBulls(totalCount)
