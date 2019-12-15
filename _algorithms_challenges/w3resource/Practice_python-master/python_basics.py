import datetime
import sys
import re
import calendar

from math import pi


def twinkle_star():
    """ 1: prints the song twinkle little star in poem format. """
    print("""Twinkle, twinkle little star,
       How I wonder what you are!
               Up above the world so high,
               Like a diamond in the sky.
Twinkle, twinkle little star,
       How I wonder what you are""")


def version_python():
    """ 2: Tells the user what version of python he's working with."""
    return sys.version


def date_now():
    """ 3: Gives you the current date and time. """
    time = datetime.datetime.now()
    time = time.strftime('date:  %b/%m/%d   time: %I:%M:%S %p')
    print("Current date and time:")
    print(time)


def area_circle():
    """ 4: Measures radius of a circle """
    rad = input("Give me the radius of the circle: ")
    rad = float(rad)
    print("the area of the circle is {}!".format(str(pi * rad ** 2)))


def flip_name():
    """ 5: flips last name before first name.
    Need sto work on how to make it capitilize.
    """
    name = str(input("Please give me your first and last name: "))
    name = name.split()
    try:
        print("""Your name flipped:

              {} {}!""".format(name[1], name[0]))
    except IndexError:
        flip_name()


def num_list_touple():
    """ 6: recieves a group of numbers and return s
    those numbers in a list and tuple.
    """
    data = input("give a group of number and we will make a list and touple: ")
    data = data.split()
    num_list = []
    for num in data:
        try:
            num = int(num)
            num_list.append(str(num))
        except ValueError:
            pass
    num_tuple = tuple(num_list)
    print("List: {}".format(num_list))
    print("Tuple: {}".format(num_tuple))


def filename_extension():
    """ 7: removes anything before the first dot. """
    filename = input("Please give us your filename: ")
    extension = filename.split(".")
    del extension[0]
    extension = "{}".format('.'.join(extension))
    print(extension)


def color_list(colors=['Red', 'Green', 'Blue', 'White',
                       'Black', 'Orange', 'Purple']):
    """ 8: Returns the first and last item of list. """
    print(colors[0], colors[-1])


def date_test():
    """ 9: takes a tuple and converts it to a 'X/X/X' format"""
    exam_st_date = input("""Please give the date in a tuple:
    (X, X, X) stardards: """)
    exam_start = exam_st_date[1:-1]
    exam_start = exam_start.split(",")
    exam_start = '/'.join(map(str, exam_start))
    print("The examination will start from: {}".format(exam_start))


def n_nn_nnn(n):
    """ 10:gets a number(n) and returns the sum of n+ nn+ nnn(ex:5+ 55+ 555)"""
    result = (n*3) + (n*20) + (n*100)
    print(result)


def helps(build_in):
    """ 11: recieves a built in function of python or one artificial
    and returns the doc on them.
    """
    print("{}:  {}".format(build_in.__name__, build_in.__doc__))


def calendar_month(year, month):
    """ 12: prints a calendar for the month of a given year and month."""
    return calendar.month(year, month)


def multi_line():
    """ 13: Prints a multi line statement and recieves a multi line entry. """
    print("""Enter your entry. Press ctrl+d when finished.

    nuzz
    """)
    entry = sys.stdin.read().strip()
    print("")
    print(entry)


def two_dates():
    """ 14: takes two dates and caculates the days beetween them.
    could be worked on that we could recieve two dates from user.
    """
    time_one = datetime.date(2016, 2, 23)
    time_two = datetime.date(2016, 5, 24)
    diff = time_two - time_one
    print("{} days".format(diff.days))


def volume_sphere(red):
    """ 15; recieves the radius of a sphere as a argument
    and returns the volume of that sphere.
    """
    try:
        red = float(red)
        volume = (4 / 3) * pi * red**3
        print("The volume of the sphere is {}!".format(round(volume, 2)))
    except ValueError:
        print("Sorry we need a int or float!")


def minus_17(num):
    """16: recieves a number and caculates the difrence between the number
    and 17.
    If the number is greater than 17 we multiply the the diffrence by two.
    """
    try:
        num = float(num)
    except ValueError:
        print("Try again we need a number>")
    else:
        if num > 17:
            total = (num - 17) * 2
        else:
            total = 17 - num
        print("The total is {}!".format(round(total, 1)))


def test_hundred(num):
    """17:Measures a number between 0 to 2500 if they are near 100,1000 or 2000
"""
    try:
        num = int(num)
    except ValueError:
        print("Try Again need number")
    else:
        if num > 0 and num <= 500:
            near = 100
        elif num > 500 and num <= 1500:
            near = 1000
        elif num > 1500 and num <= 2500:
            near = 2000
        try:
            print("Your number {} is near {}!".format(num, near))
        except UnboundLocalError:
            print("Sorry out of range!")


def three_add(num1, num2, num3):
    """ 18: recieves three numbers and returns the sum of the three.
    If all three numbers have the same the value then
    we also multiply the total by 3."
    """
    total = num1 + num2 + num3
    if num1 == num2 and num2 == num3:
        total = total * 3
    print("The total is {}!".format(total))


def is_string(string):
    """ 19: Adds Is to the begining of a string given
    if it doesn't allready start with Is.
    """
    if string[:2] == "Is":
        print(string)
    else:
        new_string = "Is{}".format(string)
        print(new_string)


def string_multi(string, num):
    """ 20: Makes num number of copies of string given. """
    string = "{} ".format(string)
    print(string*num)


def even_odd(num):
    """ 21: tests if a number is even or odd or not an integer."""
    if num % 2 == 0:
        return "{} is even!".format(num)
    elif num % 2 == 1:
        return "{} is odd!".format(num)
    else:
        return "Sorry {} is not an integer.".format(num)


def count_four(nums, look):
    """ 22: counts every time in a list when something is given """
    count = 0
    for num in nums:
        if num == look:
            count += 1
    return count


def copies_begin(string, num):
    """ 23: returns the first two letters of a given string copied
    a given amount of times.
    """
    if len(string) <= 2:
        string = string + " "
        return string * num
    else:
        copies = string[0:2] + " "
        return copies * num


def vowel_check(letter):
    """ 24: Checks to see if a given letter is a vowel. """
    letter = letter[0:1]
    lettered = letter.lower()
    if lettered in 'aeiou':
        print("{} is a vowel!".format(letter))
    else:
        print("{} is not a vowel.".format(letter))


def check_list(item, lists):
    """ 25: Checks if a given item is in a given list."""
    if item in lists:
        return True
    else:
        return False


def histogram(list_int):
    """ 26: Makes a histrogram of how much a given number is in a given list"""
    for num in range(0, 10):
        star = ""
        for ints in list_int:
            if num == ints:
                star = star + "*"
        print("{}|   {}".format(num, star))


def histogram2(list_int):
    """ 26/2: Histrogrambut up to down instead of sideways."""
    copy = list_int
    print("0|1|2|3|4|5|6|7|8|9")
    while copy:
        line = ""
        for num in range(0, 10):
            if num in copy:
                line = line + "* "
                copy.remove(num)
            else:
                line = line + "  "
        print(line)


def list_to_string(the_list):
    """ 27: turns a list into a string."""
    string_version = ""
    for item in the_list:
        string_version += str(item)
    return string_version


def only_even(numbers):
    """ 28: returns all numbers in a list if number is even
    and before 237 in the list.
    """
    new_numbers = []
    for num in numbers:
        if num == 237:
            break
        elif num % 2 == 0:
            new_numbers.append(num)
        else:
            continue
    return new_numbers


def list_vs_list(list1, list2):
    """ 29: Returns a list of every item in list1 thats not in list2."""
    unique_list1 = []
    for color in list1:
        if color in list2:
            pass
        else:
            unique_list1.append(color)
    return unique_list1


def area_triangle(base, height):
    """30: Computes the area of a triangle with thelength of base and height"""
    return (base * height) / 2


def greatest_common_divisor(int1, int2):
    """ 31: Computes the greatest common divisor of two given integer. """
    gcd = 1
    for num in range(1, int1):
        if int1 % num == 0 and int2 % num == 0:
            gcd = num
    return gcd


def least_common_multiple(int1, int2):
    """ 32: returns the least common multipleof two intigers given."""
    for num1 in range(1, 100):
        for num2 in range(1, 100):
            if int1 * num1 == int2 * num2:
                lcm = int1 * num1
                return lcm


def three_diffrent_or_zero(int1, int2, int3):
    """ 33: Returns the sum of three given numbers
    If one of the numbers are equal to the other returns Zero.
    """
    if int1 == int2 or int2 == int3 or int1 == int3:
        return "Zero"
    else:
        return int1 + int2 + int3


def sum_not(num1, num2):
    """ 34: Returns the sum of two given numbers.
    If the total is in between 15 to 20 we return 20 instead of total.
    """
    total = num1 + num2
    if total >= 15 and total <= 20:
        return 20
    else:
        return total


def equal_five(num1, num2):
    """ 35: returns True if two given numbers are equal
    or the sum or the diffrence of the two numbers are equal to 5.
    """
    if num1 == num2 or num1 - num2 == 5:
        return True
    elif num2 - num1 == 5 or num1 + num2 == 5:
        return True
    else:
        return False


def add_only_int(obj1, obj2):
    """ 36: Adds two objects together only if both are pure intigers."""
    if not(isinstance(obj1, int) and isinstance(obj2, int)):
        return "Input must be an intigers!"
    total = obj1 + obj2
    return total


def name_age_address(name, age, address):
    """ 37: Prints a person name, age and address on three diffrent lines. """
    print("My name is {}.".format(name))
    print("I am {} years old.".format(age))
    print("I leave in {}.".format(address))


def xy_squared(x, y):
    """ 38: Squares the sum of x and y (ex: (x + y)^2"""
    return (x + y) ** 2


def interest_tester(amount, int_rate, years):
    """ 39: Tells user how much interest he will owe in X amount of years
    and the total amount due.
    """
    interest = (amount / 100) * int_rate * years
    total = amount + interest
    print("The interest per {} years is {}!".format(years, interest))
    print("The total owed is {}!".format(total))
    return total


def triangle(x1, x2, y1, y2):
    """ 40: Measures the distance between two points by x^2 +y^2 = z^2. """
    x = x2 - x1
    y = y2 - y1
    distance = x**2 + y**2
    return round(distance ** 0.5, 2)


colors = ['Red', 'Green', 'Blue', 'White', 'Black', 'Orange', 'Purple']
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953,
    345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
    687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831,
    445, 742, 717, 958, 743, 527
    ]
lists = [1, 2, 5, 4, 3, 6, "n", "@", 3, 8, 5, 8, 9, 4, 8, 9, 5, 8, 3, 8, 2]
list_nuzz = ['n', 'u', 'z', 'z']

print(calendar_month(2016, 3))
