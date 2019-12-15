def maximum(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:
        return c

if __name__ == '__main__':
    a = 1
    b = 2
    c = 3

    print(maximum(a, b, c))
