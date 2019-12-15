import random
import sys
import re

# from python_lists import (make_list, make_list_num, make_str_list,
#                          make_num_str_list)


def dev7_multiply5():
    """ 1: returns all numbers in range between 1500 and 2700
    which are divisible by 5 and 7.
    """
    answer_list = []
    for number in range(1500, 2701):
        if number % 7 == 0 and number % 5 == 0:
            answer_list.append(number)
    return answer_list


def celsius_farenheit():
    """ 2: Converts celsius to farenheut and farenheit to celsius. """
    try:
        temp = int(input("Tempurate: "))
    except ValueError:
        return celsius_farenheit()
    types = input("Type C to return Celsius and F for Farenheit? ").lower()
    if types == 'c':
        nuzz = ((temp - 32) * 5) / 9
        print("{} F is {} in Celsius.".format(temp, round(nuzz)))
    elif types == 'f':
        nuzz = ((temp * 9) / 5) + 32
        print("{} C is {} in Farenheit.".format(temp, round(nuzz)))
    else:
        return celsius_farenheit()


def guess_number():
    """ 3: Game in which user guesses random number from 1 to 9."""
    computer_guess = random.randint(1, 10)
    while True:
        try:
            user_guess = int(input("Guess a number between 1 to 9: "))
        except ValueError:
            continue
        if user_guess == computer_guess:
            print("Well Guessed!")
            break


def make_two_triangle(size):
    """ 4: Returns two trianges back to back based on size given by user. """
    for num in range(0, size + 1):
        print(('* ' * num) + ('  ' * ((size - num) * 2)) + ('* ' * num))
    for num in range(1, size):
        print(('* ' * (size - num)) + ('  ' * num * 2) + ('* ' * (size - num)))


def make_triangle(size):
    """ 4: Returns a triangle."""
    for line in range(size):
        for star in range(line):
            print('* ', end='')
        print('')
    for line in range(size, 0, -1):
        for star in range(line):
            print('* ', end='')
        print('')


def reverse_word(word):
    """ 5: Returns the rverse of a word."""
    return word[::-1]


def count_even_odd(num_list):
    """ 6: returns the amount of numbers in a list is even or odd.
    Could recieve a list or tuples.
    Need to get import from practice_list to turn string into list also.
    and remove all non numbers from list
    """
    # num_list = make_list_num(num_list)
    even = 0
    odd = 0
    for num in num_list:
        if round(num) % 2 == 0:
            even += 1
        elif round(num) % 2 == 1:
            odd += 1
        else:
            pass
    print("Numbers of even numbers: {}".format(even))
    print("Numbers of odd numbers: {}".format(odd))


def print_list_and_type(liste):
    """ 7: Prints a out each item in a list and telss us what type it is.
    ex: 1452 is <class 'int'>
    """
    for thing in liste:
        print("{} is {}".format(thing, type(thing)))


def skip_3_and_6():
    """ 8: Prints out all numbers between 0 to 6 which are not 3 or 6."""
    for num in range(0, 7):
        if num != 3 and num != 6:
            print("{} ".format(num), end="")
    print("")


def fibonacci_sequence(num):
    """ 9: Caculates the fibanocci sequence up to a given number. """
    fibo_list = [0, 1]
    while fibo_list[-1] < num + 1:
        print("{},".format(fibo_list[-1]), end=" ")
        fibo_list.append(fibo_list[-2] + fibo_list[-1])


def fizzbuzz(num):
    """" 10: Returns the all numbers from 0 to a given number.
    All numbers devisiable by 3 we replace the number by Fizz,
    divisiable by 5 we print Buzz and if divisable by 5 and 3 we print FizzBall
    """
    for number in range(num + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz", end=", ")
        elif number % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(number, end=", ")


def two_dimension(row, column):
    """ 11: Returns a two dimensional list with based on two given param.
    Each with numbers which is row(num) * column(num)
    """
    two_d = []
    for num in range(row):
        two_d.append([])
        for num2 in range(column):
            two_d[num].append(num * num2)
    return two_d


def many_lines_input():
    """ 12: Recieves many lines from user and returns it all lowercase. """
    print("Enter your multi line entry. Press ctrl+d when finished.")
    data = sys.stdin.read().strip()
    print("Saved successfully!")
    return data.lower()


def bytess(digit=2):
    """ 13: Returns bytes thaat are devisible by 5."""
    items = []
    num = input("Numbers please: ").split(',')
    for p in num:
        x = int(p, digit)
        if x % 5 == 0:
            items.append(p)
    print(','.join(items))


def len_string_digits(string):
    """ 14: accepts a string and caculates the number of digits and letters."""
    digits = 0
    letters = 0
    for letter in string:
        try:
            int(letter)
            digits += 1
        except ValueError:
            if letter not in " !@#$%^&*()_-+=[]{}?/><.,;:\|":
                letters += 1
    print("Letters {}".format(letters))
    print("Digits {}".format(digits))


def password_validator(password):
    """ 15: Checks to wee if a given password is exceptable.
    Password needs to be 6 to 16 letters long and have at least one lowercase
    letter, one uppercase letter, one number and one of these '$#@'.
    """
    good_password = False
    if len(password) > 5 and len(password) < 17:
        if not re.search("[a-z]", password):
            pass
        elif not re.search("[A-Z]", password):
            pass
        elif not re.search("[0-9]", password):
            pass
        elif not re.search('[$#@]', password):
            pass
        else:
            good_password = True
    if good_password:
        print("Good password!")
    else:
        print("Bad password!")


def even_num_between_100_400():
    """ 16: Returns all even numbers between 100 and 400."""
    for number in range(100, 399, 2):
        print("{},".format(number), end=" ")
    print("400.")


password_validator("Hello!12@")
