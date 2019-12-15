def number_syllables(word):
    return word.count("-") + 1


def test():
    print("test has started")
    if number_syllables("syl-la-bles") != 3:
        print("error1")
    if number_syllables("pas-try") != 2:
        print("error2")
    if number_syllables("to-ma-to") != 4
        print("error3")
