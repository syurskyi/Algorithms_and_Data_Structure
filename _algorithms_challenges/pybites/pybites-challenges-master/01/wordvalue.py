from data import DICTIONARY, LETTER_SCORES


def load_words():
    """
    :return: Loads in the dictionary (text file, with each word on a new line)
    """
    file = open(DICTIONARY, 'r')
    words = file.read().split('\n')[:-1]    # Remove blank line at the end
    return words

def calc_word_value(word):
    """
    :param word: A single word string containing only alphabet characters
    Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES
    """
    upper_word = list(word.upper())
    word = ''.join(letter for letter in upper_word if letter.isalnum())
    word_score = 0


    # Is there a better way to do this than a loop?
    for letter in word:
        word_score += LETTER_SCORES[letter]

    return word_score


def max_word_value(dictionary=[]):
    """
    :param dictionary: List of words. If none provided uses default DICTIONARY
    :return: Calculate the word with the max value in the dictionary.
    """
    if dictionary == []:
        dictionary = load_words()
    print(len(dictionary))
    best_word = ''
    tied_words = []
    best_score = 0

    for word in dictionary:
        score = calc_word_value(word)
        if score < best_score:
            continue
        elif score > best_score:
            best_word = word
            best_score = score
            tied_words = []
        elif score == best_score:
            tied_words.append(word)
        else:
            print('for loop in max_word_value() is broken.')

    return best_word


if __name__ == "__main__":
    max_word_value()
