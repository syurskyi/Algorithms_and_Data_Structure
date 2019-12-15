import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        guess = input('Your guess: ')
        if not guess:
            print('Please enter a number')
            raise ValueError('Nothing entered')
        if not all(c.isdigit() for c in str(guess)):
            print('Should be a number')
            raise ValueError('Non-digit entered')
        guess = int(guess)
        if not (START <= guess <= END):
            print('Number not in range')
            raise ValueError('Out of range')
        if guess in self._guesses:
            print('Already guessed')
            raise ValueError('Retry previous guess')
        self._guesses.add(guess)
        return guess

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess == self._answer:
            print(f'{guess} is correct!')
            return True
        elif guess < self._answer:
            print(f'{guess} is too low')
        else:
            print(f'{guess} is too high')
        return False

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while len(self._guesses) < MAX_GUESSES and not self._win:
            try:
                this_guess = self.guess()
            except ValueError:
                continue
            if self._validate_guess(this_guess):
                self._win = True
                return
        print(f'Guessed {MAX_GUESSES} times, answer was {self._answer}')
        return


if __name__ == '__main__':
    game = Game()
    game()
