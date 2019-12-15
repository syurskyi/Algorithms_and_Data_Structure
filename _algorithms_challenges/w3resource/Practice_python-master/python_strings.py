import re


def length(string):
    """1:Caculates the length of any string,Also could do this with len(str)"""
    count = 0
    for letter in string:
        count += 1
    return count


def count_every_letter(string):
    """ 2: counts every letter, symbol and number in a given string. """
    results = {}
    for letter in string:
        if letter in results:
            results[letter] += 1
        else:
            results[letter] = 1
    return results


def first2_last2(string):
    """ 3: returns a string with the first two and last chars from given string
    If the string is less than two char it returns 'Empty String'
    """
    if len(string) < 2:
        return "Empty String"
    else:
        return "{}{}".format(string[0:2], string[-2:])


def change_repeat(word):
    """ 4: replaces any re used letter in a string into a $. """
    word = list(word)
    used = []
    index = 0
    for letter in word:
        if letter in used:
            word[index] = '$'
        else:
            used.append(letter)
        index += 1
    return ''.join(word)


def swap_beginning(string1, string2):
    """ 5: Takes in two strings and returns it in one sring and swaps the first
    two letters of each word with the other. (ex: 'abc', 'xyz' = 'xyc abz')
    """
    new1 = string1[:2] + string2[2:]
    new2 = string2[:2] + string1[2:]
    return "{} {}".format(new1, new2)


def ingly(word):
    """ 6: Adds a 'ing' to the end of a given word.
    If the word allready ends with 'ing' we add 'ly instead.
    """
    if word[-3:] == 'ing':
        new_word = word + 'ly'
    else:
        new_word = word + 'ing'
    return new_word


def not_bad_good(string):
    """ 7: Recieves a string from user and if the sentence has not
    and then later bad we replace everything between them woth good!
    ex: 'The lyrics are not that bad!' = 'The lyrics are good!'
    """
    sentence = string.split()
    snot = string.find('not')
    sbad = string.find('bad')
    if sbad > snot:
        sentence = string.replace(string[snot:(sbad + 3)], 'good')
    else:
        sentence = string
    return sentence


def longest_word(lists):
    """ 8: Shows the longest word or words in a sentence! """
    lists = lists.split()
    longest = ''
    extra = ''
    for word in lists:
        if len(word) > len(longest):
            longest = word
            extra = ''
        elif len(word) == len(longest):
            extra += ", {}".format(word)
    print("The longest word in your sentence is {}!".format(len(longest)))
    print("These are the word:")
    return "        {}".format(longest + extra)


def remove_n(string, n):
    """ 9: Removes a given letter by by the number given."""
    words = list(string)
    del words[n-1]
    return ''.join(words)


def life_is_(string):
    """ 10: Swaps the first letter with the last letter of a given word."""
    new_string = string[-1:] + string[1:-1] + string[:1]
    return new_string


def remove_odd_index(string):
    """ 11: removes all odd index value form a given string."""
    new_string = string[1::2]
    return new_string


def count_word(sentence):
    """ 12: counts the amount of words in a program"""
    counts = dict()
    words = sentence.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_word("Hello world I love the world, the world is great"))
        


def upper_lower():
    """ 13: Gets an input from user and makes it uppercaes and lowercase."""
    scr = input("Please give us a string so we could upper and lowercase it: ")
    lower_script = scr.lower()
    upper_script = scr.upper()
    print(lower_script)
    return upper_script


def sorted_alphabet(lists):
    """ 14: Sorts a list alphabetically not showing prefrence
    of uppercase over lowercase.
    Only will work if one adds a string of words seperated by ', '.
    """
    lists = lists.split(', ')
    lists = sorted(lists, key=str.lower)
    return ', '.join(lists)


def add_tags(letter, string):
    """ 15: Adds html like tags to a given string with a given tag."""
    return "<{}>{}</{}>".format(letter, string, letter)


def insert_string_middle(string1, string2):
    """ 16: Puts one string in middle of the another. """
    begin = string1[:round(len(string1)/2)] + string2
    return begin + string1[round(len(string1)/2):]


def insert_end(string):
    """ 17: Returns the last to letters of a given string copied four times
    like: 'eseseses'
    """
    if len(string) >= 2:
        return 4 * string[-2:]
    return "Sorry string needsto be at least two letters long!"


def first_three(string):
    """ 18: Returns the frst three letters of a given string. """
    return string[:3]


def string_first_half(string):
    """ 19: Returns first half of a given string.
    If the string only has one letter we return the string alone.
    """
    if len(string) == 1:
        return string
    return string[:round(len(string)/2)]


def reverse_if_four(string):
    """ 20: Reverses a given string if the length of the string
    is a multiple of 4.
    """
    if len(string) % 4 == 0:
        return string[::-1]
    return string


def upper_two_four(string):
    """ 21: Caps a string given if two letters in the first four letters
    of the string are capitial.
    """
    first_four = string[:4]
    capital = re.findall(r'[A-Z]', first_four)
    if len(capital) >= 2:
        return string.upper()
    else:
        return string


print(insert_string_middle('{{N}}', 'Nuzz'))
