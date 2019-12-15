# Guess Letters - Hangman 02: unsure why

# Greeting
if __name__ == '__main__':
    # Welcome Message
    print("Welcome to hangman!")
    # Define variables
    word = "EVAPORATE"
    guessed = "_" * len(word)
    # Turn variables into lists
    word = list(word)
    guessed = list(guessed)
    lstGuessed = []
    # Input
    letter = input("Choose a letter: ")
    # Outputs
    while True:
        # Scenario 1: Letter already guessed
        if letter.upper() in lstGuessed:
            letter = ''
            print("Already guessed!")
        # Scenario 2: Letter is correct, replaces _
        elif letter.upper() in word:
            # Index: turns a string "Word" into indices "W-O-R-D"
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = '_'
        # Scenario 3:
        else:
            # don't quite understand
            # Correct letter is join(guessed), displayed
            print(''.join(guessed))
            if letter is not '':
                # Wrong letter is added to lstguessed
                lstGuessed.append(letter.upper())
            # Choose the next letter
            letter = input("Choose a letter: ")
        # Scenario 4: All _ is replaced
        if '_' not in guessed:
            print("You won!!")
            break
