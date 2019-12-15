from functools import reduce
# import string
# import re


# 1 use reduce to return the highest number of many numbers.
def max_of_two(num1, num2):
    """return sthe highest of two given numbers. """
    if num1 > num2:
        return num1
    return num2

# print(reduce(max_of_two, [1,-9,3]))


# 2 Uses reduce again to add a whole group of numbers
def add(num1, num2):
    """adds two numbers together. """
    return num1 + num2


def reducer(func, lists):
    """uses reduce against a given function and list"""
    return reduce(func, lists)
# print(reducer(max_of_two, (8,2,3,0,7)))


# 3: uses reduce to add a list of numbers together.
def multiply(num1, num2):
    """Multiplies two numbers  """
    return num1 * num2
# print(reduce(multiply, (8, 2, 3, -1,7)))


# 4
def reverses(string):
    """Reverses the order of every letter in a string """
    reverse_string = list(reversed(string)).copy()
    return ''.join(reverse_string)

# print(reverses("1234abcd"))


# 5
def factorial(the_num):
    """ Return the factorial of a given number or the fsctorial its near."""
    try:
        the_num = int(the_num)
    except ValueError:
        return "sorry numbers only"
    num = 1
    num_list = [1]
    while True:
        total = 1
        for number in num_list:
            total *= number
        total *= (num + 1)
        if total == the_num:
            return "{}!".format(num + 2)
        elif total > the_num:
            return "Not a factorial: between {}! and {}!".format(num + 1,
                                                                 num + 2)
        num += 1
        num_list.append(num)

# print(factorial(25))


# 6
def num_in_range(num, begin, end):
    """ returns True if a given number is in a given range """
    if num in range(2, 9):
        return True
    else:
        return False

# print(num_in_range(3, 2, 9))


# 7
def upper_or_lower(string):
    """ returns the numbers of uppercase letters and lowercase. """
    upper = 0
    lower = 0
    for letter in string:
        if letter.isalpha():
            if letter == letter.upper():
                upper += 1
            elif letter == letter.lower():
                lower += 1
    return "They are {} uppercase letters and {} lowercase letters.".format(
                                                                upper, lower)

# print(upper_or_lower('The,{} quick Brow Fox'))


# 8
def only_unique(normal_list):
    """ Removes all repeations ina given list."""
    unique_list = []
    for item in normal_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# print(only_unique([1,2,3,3,3,'n','m','n',3,4,5]))


# 9
def is_prime(num):
    """ Tests if a given number is prime. """
    if num < 2:
        return False
    for num1 in range(2, num - 1):
        for num2 in range(2, num - 1):
            if num1 * num2 == num:
                return False
    return True

# print(is_prime(8))


# 10
def even_list(all_list):
    """ Returns all even items in a list """
    return [num for num in all_list if num % 2 == 0]

# print(even_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 11
def perfect_number_checker(num):
    """Tells you if a number is a perfect number in number theory.
    6, 28, 496 and 8128 are perfect numbers.
    """
    divisors = [divisor for divisor in range(1, num) if num % divisor == 0]
    total = 0
    for number in divisors:
        total += number
    if total == num and (total + num) / 2 == num:
        print("{} is a perfect Number!!!!!!".format(num))
        return True
    else:
        print("{} is not a perfect number or an imperfect! BOOOO!".format(num))
        return False

# print(list(map(perfect_number_checker, [6, 7, 24, 28, 87, 496])))


# 12
def pailindrome_checker(phrase):
    """ checks if a word or phrase is a pailindrome is the same if you flip"""
    string = phrase.split().copy()
    string = ''.join(string)
    if reverses(string) == string:
        return "'{}' is a pailindrome!".format(phrase)
    else:
        return "Sorry '{}' is not a pailindrome!".format(phrase)

# print(pailindrome_checker("madam"))


# 13
def pascals_triangle(size):
    """retiurns a list of alll the numbers in a pascals triangle with 'size'
    amount of rows. Also prints out each sublist on diffrent lines.
    """
    listed = [[1]]
    for num in range(1, size):
        nuzz = []
        for n in range(0, num+1):
            if n - 1 < 0:
                nerd = 1
            else:
                try:
                    nerd = (listed[-1][n] + listed[-1][n-1])
                except IndexError:
                    nerd = 1
            nuzz.append(nerd)
        listed.append(nuzz)
    for x in range(0, len(listed)):
        print(listed[x])
    return listed

# pascals_triangle(10)


# 14
def pangram(sentence):
    """ Returns True if a given sentence is a pangram and False otherwise.
    (pangram is if a given sentence has every letter in the alphabet.
    """
    low_sen = sentence.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pangram_list = []
    for letter in low_sen:
        if letter not in pangram_list and letter in alphabet:
            pangram_list.append(letter)
    if len(pangram_list) == len(alphabet):
        return True
    else:
        return False

print(pangram("The quick browwwwwn fox jumps over the lazy dog"))


# 15
def sort_hyphen(hyphen):
    """ Sorts item in a given sequence alphabetically whuch each item is
    seperated by an hyphen.
    """
    hyphen_list = hyphen.split("-")
    hyphen_list = sorted(hyphen_list)
    return '-'.join(hyphen_list)

# print(sort_hyphen("green-red-yellow-black-white"))


# 16
def squared(num=30):
    """Returns all numbers squared between 1 to the given number or 30."""
    [print(n**2) for n in range(1, num+1)]

# squared()
