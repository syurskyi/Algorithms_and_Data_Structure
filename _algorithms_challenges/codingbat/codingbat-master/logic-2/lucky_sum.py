''' Given 3 int values, a b c, return their sum. However, if one of the values
is 13 then it does not count towards the sum and values to its right do not
count. So for example, if b is 13, then both b and c do not count. '''


def lucky_sum(a, b, c):
    ints_sum = 0
    for num in [a, b, c]:
        if num == 13:
            break
        ints_sum += num
    return ints_sum
