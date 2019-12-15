#! /Users/piotrjankiewicz/anaconda3/bin/python3.6

def guess(options):
    possible = options

    if len(possible) == 1:
        print('The guess has to be: %s' % (possible[0]))
        return

    index = int(len(possible) / 2)
    currentGuess = possible[index]
    print('Computer guesses: %s' % currentGuess)
    feedback = input('To big ? (bigger) To small? (smaller) ? Good guess? (equal)\n')

    allowed = ['bigger', 'smaller', 'equal']

    if feedback not in allowed:
        print('Uknown command :(')
        guess(possible)
    elif feedback == allowed[0]:
        if currentGuess == 100:
            print("Can't be bigger! It has to be %s" % currentGuess)
            return
        guess(possible[index + 1:len(possible)])
    elif feedback == allowed[1]:
        guess(possible[0:index])
    elif feedback == allowed[2]:
        print('Yes! I am a smart program!')
        return


if __name__ == '__main__':
    guess(range(0, 101))
