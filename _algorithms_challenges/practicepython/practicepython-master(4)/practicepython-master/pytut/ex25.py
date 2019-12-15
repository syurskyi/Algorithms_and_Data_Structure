def break_words(stuff):
    """This function will break words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)


def print_first_word(words):
    """prints the first word after popping it off"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_word(words)


def print_first_and_last(sentence):
    """Prints first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words and prints the first and the last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

    
