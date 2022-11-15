
def tail(n):

    print('Calling tail with n=' + str(n))

    # BASE CASE
    if n == 0:
        return

    # first of all we do some operations
    # operation = print()
    print(n)

    # make the recursive function call
    tail(n-1)


def head(n):

    print('Calling head() with n=' + str(n))

    if n == 0:
        return

    # we make the recursive function call
    head(n-1)

    # we can do any operations
    # operation - print()
    print(n)


head(5)
