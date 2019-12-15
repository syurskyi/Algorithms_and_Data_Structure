''' Return True if the string "cat" and "dog" appear the same number of times
in the given string. '''


def cat_dog(str):
    cats = 0
    dogs = 0
    for i, _ in enumerate(str):
        if str[i:i + 3] == 'cat':
            cats += 1
        if str[i:i + 3] == 'dog':
            dogs += 1
    if cats == dogs:
        return True
    return False
