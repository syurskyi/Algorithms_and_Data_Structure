
def make_list(lists):
    """ 0: Makes sure item given is a list and if not will make it a list
    Should add a way to convert tuples into list.
    """
    if (isinstance(lists, list)):
        return lists
    try:
        return lists.split()
    except AttributeError:
        lists = lists.remove("(", ")")


def make_list_num(lists):
    """ 0.25: Makes a list and makes all item into a int unless not a number.
    Then we just delete that item.
    """
    lists = make_list(lists)
    new_lists = []
    for item in lists:
        try:
            new_lists.append(float(item))
        except ValueError:
            continue
    return new_lists


def make_str_list(lists):
    """ 0.5: Makes everything in the list into a string. """
    lists = make_list(lists)
    new_list = []
    for item in lists:
        new_list.append("{}".format(item))
    return new_list


def make_num_str_list(lists):
    """ 0.75: Makes any number a number and any thing not a string in a list"""
    lists = make_list(lists)
    new_list = []
    for item in lists:
        try:
            new_list.append(float(item))
        except ValueError:
            new_list.append(item)
    return new_list


def length_list(lists):
    """ 1: returns the number of amounts of a given list."""
    lists = make_list(lists)
    return len(lists)


def multiply_list(lists):
    """ 2: Multiples all the items in the list."""
    lists = make_list_num(lists)
    total = 1
    for number in lists:
        total = total * number
    return round(total)


def largest_number(lists):
    """ 3: Returns the largest number in a list."""
    lists = make_list_num(lists)
    large = 0
    for num in lists:
        if num > large:
            large = num
    return round(large)


def smallest_number(lists):
    """ 4: Returns the smallest number in a list. """
    lists = make_list_num(lists)
    small = 10000000000000000000000000000
    for num in lists:
        if num < small:
            small = num
    return round(small)


def first_last_equal(lists):
    """ 5: Returs all word in lists that start and end with the same
    letter/number if the word has 2 or more letters/numbers.
    """
    lists = make_list(lists)
    count = 0
    for item in lists:
        if len(item) > 1:
            if item[0] == item[-1]:
                count += 1
    return count


def six():
    pass


def remove_duplicates(lists):
    """ 7: Remove any duplicates in a list."""
    lists = make_list(lists)
    new_lists = []
    for word in lists:
        if word not in new_lists:
            new_lists.append(word)
    return new_lists


def check_if_empty(lists):
    """ 8: Checks to see if a list is empty of not."""
    lists = make_list(lists)
    if len(lists):
        print("This list contains stuff!")
        return True
    else:
        print("Empty!!!! Nothing here!")
        return False


def clone_list(lists):
    """ 9: Makes a clone or copy of a given list."""
    lists = make_list(lists)
    new_lists = list(lists)
    return lists, new_lists


def far_away(lists, num, word):
    """ 10: Deletes all items in a given list that are nth distance away
    from a certian list.
    """
    lists = make_list(lists)
    for index, thing in enumerate(lists):
        if thing == word:
            del lists[index - num:index + num + 1]
    return lists


def one_common_member(list1, list2):
    """ 11: Returns True if list1 has one common item as list2. """
    list1 = make_list(list1)
    list2 = make_list(list2)
    for item in list1:
        if item in list2:
            return True
    return False


def remove_0245(lists):
    """ 12: Removes the 0th, 2nd, 4th and 5th index ina given list. """
    lists = make_list(lists)
    return lists[1:2] + lists[3:4] + lists[6:]


def threed_array():
    """ 13: makes a 3-D array element like a math tuple, 3-D list of *
    and picture with *.
    """
    threed_list = []
    for row in range(1, 4):
        for column in range(1, 5):
            for page in range(1, 7):
                threed_list.append("({},{},{})".format(row, column, page))
    a = ([[['*' for col in range(3)] for col in range(4)] for row in range(6)])
    for row in range(3):
        print(("* " * 4 + "    ") * 6)
    return threed_list, a


def remove_all_even(num_list):
    """ 14: Removes all even numbers from a list. """
    num_list = make_list_num(num_list)
    new_num_list = []
    for num in num_list:
        if round(num) % 2 == 0:
            continue
        else:
            new_num_list.append(num)
    return new_num_list


def sort_list(listed):
    """ 14.5: Sorts a list by number first then by alphabetical number. """
    listed = make_str_list(listed)
    listed.sort(key=str.lower)
    listed = make_num_str_list(listed)
    print(listed)


def shuffle_list(listed):
    """ 15: Shuffles a list presenting it into a random order."""
    from random import shuffle
    listed = make_list(listed)
    shuffle(listed)
    return listed


def square_to_25():
    """ 16: Returns a list of numbers squared from 2 to 25. """
    square_list = []
    for num in range(2, 26):
        square_list.append(num**2)
    return square_list


def square_from6_to30():
    """ 17: Returns a list of numbers squared from 6 to 30. """
    square_list = []
    for num in range(6, 31):
        square_list.append(num**2)
    return square_list
