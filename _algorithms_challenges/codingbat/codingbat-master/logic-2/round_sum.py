''' For this problem, we'll round an int value up to the next multiple of 10 if
its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round
down to the previous multiple of 10 if its rightmost digit is less than 5,
so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded
values. To avoid code repetition, write a separate helper "def round10(num):
and call it 3 times. Write the helper entirely below and at the same indent
level as round_sum(). '''


def round_sum(a, b, c):
    ints_sum = 0
    for num in [a, b, c]:
        ints_sum += round10(num)
    return ints_sum


def round10(num):
    last_digit = int(str(num)[-1])
    if last_digit >= 5:
        return num + 10 - last_digit
    return num - last_digit
