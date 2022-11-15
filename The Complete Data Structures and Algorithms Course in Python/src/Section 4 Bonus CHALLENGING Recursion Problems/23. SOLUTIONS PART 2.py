# REVERSE SOLUTION


def reverse(strng):
    if len(strng) <= 1:
        return strng
    return strng[len(strng) - 1] + reverse(strng[0:len(strng) - 1])


# IS PALINDROME SOLUTION


def isPalindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng) - 1]:
        return False
    return isPalindrome(strng[1:-1])


# SOME RECURSIVE SOLUTION


def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not (cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True


def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


# FLATTEN SOLUTION


def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else:
            resultArr.append(custItem)
    return resultArr