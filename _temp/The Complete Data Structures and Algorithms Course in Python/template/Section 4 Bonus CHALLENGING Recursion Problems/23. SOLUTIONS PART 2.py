# REVERSE SOLUTION


___ reverse(strng
    __ l..(strng) <_ 1:
        r_ strng
    r_ strng[l..(strng) - 1] + reverse(strng[0:l..(strng) - 1])


# IS PALINDROME SOLUTION


___ isPalindrome(strng
    __ l..(strng) __ 0:
        r_ T..
    __ strng[0] !_ strng[l..(strng) - 1]:
        r_ F..
    r_ isPalindrome(strng[1:-1])


# SOME RECURSIVE SOLUTION


___ someRecursive(arr, cb
    __ l..(arr) __ 0:
        r_ F..
    __ n.. (cb(arr[0]
        r_ someRecursive(arr[1:], cb)
    r_ T..


___ isOdd(num
    __ num _ 2 __ 0:
        r_ F..
    ____
        r_ T..


# FLATTEN SOLUTION


___ flatten(arr
    resultArr _    # list
    ___ custItem __ arr:
        __ type(custItem) __ list:
            resultArr.extend(flatten(custItem))
        ____
            resultArr.a..(custItem)
    r_ resultArr