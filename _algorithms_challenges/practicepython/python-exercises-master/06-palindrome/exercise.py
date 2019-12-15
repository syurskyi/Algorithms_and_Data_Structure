#/#! /urs/bin/env python

if __name__ == '__main__':
    firstWord = str(raw_input('Give me a first word: '))
    firstWord = firstWord.replace(" ","")

    firstWordBackword = firstWord[::-1]

    if firstWord == firstWordBackword:
        print("The word %s is a palindrome! (%s)"%(firstWord, firstWordBackword))
    else:
        print("The word %s is not a palindrome! (%s)"%(firstWord, firstWordBackword))