def divisible(num):
    if num >= 100 and num % 100 == 0:
        return True
    elif num == 0:
        return True
    elif num < 0 and num % 100 == 0:
        return True
    else:
        return False
