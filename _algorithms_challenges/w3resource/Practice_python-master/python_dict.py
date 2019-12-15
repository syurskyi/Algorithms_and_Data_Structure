def sort_dict(the_dict):
    """ 1: sorts a dict bty vakues and returns that dict.
    Assumes youu use numbers as keys so it returns numbers (should fix that).
    """
    print(the_dict)
    sorted_dict = {}
    reversed_dict = {}
    sorted_list = sorted(the_dict.values())
    count = 1
    for word in sorted_list:
        sorted_dict[count] = word
        count += 1
    reversed_list = sorted(the_dict.values(), reverse=True)
    for word in reversed_list:
        reversed_dict[count] = word
        count += 1
    return sorted_dict, reversed_dict


def add_to_dict(the_dict):
    """ 2: Allows user to add key and values to given dictionary."""
    while True:
        key = input("What key do you want to add? If none press enter: ")
        value = input("What value do you want to add? ")
        if key:
            the_dict[key] = value
        else:
            the_dict[len(the_dict)+1] = value
        done = input("Are you done? Press d,q or s to stop: ")
        if done == 'd' or done == 's' or done == 'q':
            return the_dict


def one_big_dict(dic1, dic2, dic3):
    """ 3: Combines three dict in one. """
    new_dict = {}
    for dic in (dic1, dic2, dic3):
        new_dict.update(dic)
    return new_dict

# print(one_big_dict({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}))


def one_big_dict2(dic1, dic2, dic3):
    """ 3: For 3.5 version of python, this code workd better to combine dict"""
    new_dict = {**dic1, **dic2, **dic3}
    return new_dict


def check_key(the_dict, check):
    """ 4: checks if a given thing is a key in a given dict. """
    for key in the_dict:
        if key == check:
            return True
    return False


def loop_dict(dic):
    """ 5: Prints every pair in a given dict by 'key: value'. """
    for key, value in dic.items():
        print("{}: {}".format(key, value))


def square_dict_maker(num):
    """ 6: returns a dict with keys which values are squared value of key.
    Key go from one till number given by user.
    """
    square_dict = {}
    for times in range(1, num + 1):
        square_dict[times] = times**2
    return square_dict


def square_dict_15():
    """7: Returns a dict with key numbers 1 to 15 and values the key squared"""
    square_dict = {}
    for key in range(1, 16):
        square_dict[key] = key**2
    return square_dict


def merge_three_dict(dic1, dic2, dic3):
    """ 8: Put three dicts into one big one and label dict by number. """
    merge_dict = {}
    merge_dict[1] = dic1
    merge_dict[2] = dic2
    merge_dict[3] = dic3
    return merge_dict


# print(merge_three_dict({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}))
# print(loop_dict({'meow': 'hey', 'asd': 'nuzz', 3:'as'}))
# print(one_big_dict({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50,6: 60}))
